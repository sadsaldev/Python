import yt_dlp
import os

def download_video(url, download_path, file_format):
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
    }
    
    if file_format == 'mp4':
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
        
    elif file_format == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        print('Formato no soportado. Usa mp4 o mp3')
        return
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'Archivo descargado en {download_path}')
    except Exception as e:
        print(f'Error: {e}')
        
if __name__ == '__main__':
    while True:
        url = input('Introduce la URL del video de YouTube (o escribe "salir" para terminar): ')
        if url.lower() == 'salir':
            print('Saliendo del programa...')
            break
        download_path = input('Introduce la ruta de descarga (Carpeta donde quieres que se descargue el archivo)')
        file_format = input('Introduce el formato de descarga (mp3/mp4)').lower()
    
        download_video(url, download_path, file_format)