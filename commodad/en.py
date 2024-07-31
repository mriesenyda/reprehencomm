  import webbrowser

  def open_url(url):
      try:
          webbrowser.open(url)
          print(f"Opened URL successfully: {url}")
      except Exception as e:
          print(f"Error opening URL: {str(e)}")
  