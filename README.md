# YouTube Downloader Pro

This project was fully created with the help of AI tools, embracing the "vibe coding" approach to streamline development and creativity.
A modern, responsive web application for downloading YouTube videos and playlists. Built with Django and yt-dlp.

## Features

- Download YouTube videos in MP4 format
- Download YouTube videos as MP3 audio
- Support for playlists and channels
- Multiple quality options
- Dark/Light theme
- Download history tracking
- Progress tracking
- Responsive design for mobile devices

## Disclaimer:  
This project is a work in progress and may not function as expected in all scenarios. While it was developed entirely using AI tools to embrace innovation and creativity, some features might not work as intended. Feel free to experiment and improve upon it, but remember to maintain the AI-driven development approach for consistency and originality.  
Happy coding!

## Prerequisites

- Python 3.8 or higher
- FFmpeg (for MP3 downloads and high-quality MP4 downloads)
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd youtube-downloader
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Install FFmpeg:
   - Download FFmpeg from [FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases)
   - Extract the ZIP file
   - Copy the contents of the 'bin' folder to 'C:\ffmpeg\bin\'
   - Add 'C:\ffmpeg\bin' to your system's PATH environment variable

5. Run database migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Open your web browser and navigate to `http://127.0.0.1:8000`

## Usage

1. Enter a YouTube URL in the input field
2. Choose the desired format (MP4 or MP3)
3. Select the quality
4. For playlists, check the "Download as Playlist" option
5. Click the Download button
6. Wait for the download to complete
7. The downloaded file will be saved in the `media/downloads` directory

## Development

The project structure is organized as follows:

```
youtube-downloader/
├── downloader/              # Main app directory
│   ├── templates/          # HTML templates
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   └── urls.py            # URL routing
├── media/                  # User-uploaded files
│   └── downloads/         # Downloaded videos
├── static/                # Static files (CSS, JS, images)
├── youtube_downloader/    # Project settings
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 