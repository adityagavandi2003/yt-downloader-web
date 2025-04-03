import os
import time
import logging
from datetime import datetime, timedelta
from django.conf import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def clean_old_files():
    """Clean up files older than 1 hour"""
    try:
        # Get the downloads directory path
        downloads_dir = os.path.join(settings.BASE_DIR, 'downloads')
        
        # Ensure the directory exists
        if not os.path.exists(downloads_dir):
            logging.warning(f"Downloads directory not found: {downloads_dir}")
            return
        
        # Get current time
        current_time = datetime.now()
        # Set threshold to 1 hour ago
        threshold = current_time - timedelta(hours=1)
        
        # Counter for cleaned files
        cleaned_count = 0
        
        # Iterate through files in the directory
        for filename in os.listdir(downloads_dir):
            file_path = os.path.join(downloads_dir, filename)
            
            # Skip if it's a directory
            if os.path.isdir(file_path):
                continue
            
            # Get file modification time
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            # Check if file is older than threshold
            if file_mtime < threshold:
                try:
                    os.remove(file_path)
                    cleaned_count += 1
                    logging.info(f"Cleaned old file: {filename}")
                except Exception as e:
                    logging.error(f"Error cleaning file {filename}: {str(e)}")
        
        logging.info(f"File cleanup completed. {cleaned_count} files removed.")
        
    except Exception as e:
        logging.error(f"Error during file cleanup: {str(e)}")

def run_cleanup():
    """Run the cleanup process"""
    while True:
        try:
            clean_old_files()
            # Wait for 1 hour before next cleanup
            time.sleep(3600)  # 3600 seconds = 1 hour
        except Exception as e:
            logging.error(f"Error in cleanup process: {str(e)}")
            # Wait for 5 minutes before retrying
            time.sleep(300)  # 300 seconds = 5 minutes

if __name__ == '__main__':
    run_cleanup() 