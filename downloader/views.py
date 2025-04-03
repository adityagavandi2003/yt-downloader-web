from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST  # Fixed typo: Changed require_POSTsd to require_POST
from django.conf import settings
import yt_dlp
import os
import re
import logging
from .models import DownloadHistory

# Configure logging using Django's settings
logger = logging.getLogger(__name__)

# Download directory
DOWNLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def sanitize_filename(filename):
    """Sanitize filenames to prevent security issues."""
    return re.sub(r'[<>:"/\\|?*]', '', filename).replace(' ', '_')

@csrf_exempt
def get_video_info(request):
    """Fetch video information."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
    url = request.POST.get('url')
    if not url:
        return JsonResponse({'error': 'URL is required'}, status=400)
    
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            if not info:
                return JsonResponse({'error': 'Failed to fetch video info'}, status=400)
            
            return JsonResponse({
                'title': info.get('title', 'Untitled'),
                'thumbnail': info.get('thumbnail', ''),
                'duration': info.get('duration', 0),
                'filesize': info.get('filesize', 0),
            })
    except Exception as e:
        logger.error(f"Error fetching video info: {e}")
        return JsonResponse({'error': str(e)}, status=500)

@require_POST
def download_video(request):
    """Download video."""
    url = request.POST.get('url')  # Ensure this retrieves the URL correctly
    format_type = request.POST.get('format', 'mp4')
    quality = request.POST.get('quality', 'best')

    if not url:
        return JsonResponse({'error': 'URL is required'}, status=400)

    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = sanitize_filename(f"{info['title']}.{format_type}")
            file_path = os.path.join(DOWNLOAD_DIR, filename)
            return JsonResponse({'file_path': file_path})
    except Exception as e:
        logger.error(f"Error downloading video: {e}")
        return JsonResponse({'error': str(e)}, status=500)

def index(request):
    """Render the main page."""
    history = DownloadHistory.objects.all().order_by('-date')[:10]
    return render(request, 'downloader/index.html', {'history': history})

# Add this function to handle progress tracking
def get_progress(request):
    """Return the progress of the current download."""
    # Example implementation: Replace with actual progress tracking logic
    progress = {
        'status': 'in_progress',  # Possible values: 'in_progress', 'completed', 'error'
        'percentage': 50,        # Replace with actual percentage
    }
    return JsonResponse(progress)







