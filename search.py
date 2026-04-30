from youtube_search import YoutubeSearch

def search_media(text, page=10):
    results = YoutubeSearch(text, max_results=page).to_dict()
    txt = ''
    for video in results:
        txt += f"عنوان: {video['title']}\n"
        txt += f"https://youtube.com/watch?v={video['id']}\n"
        txt += f"کانال: {video['channel']}\n"
        txt += "————–————–\n"
    return txt
