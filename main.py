from playwright.sync_api import sync_playwright


def get_transcription(URL: str, time: bool) -> None:
    with sync_playwright() as p:
        print(f"Getting transcription... Please be patient and wait!")

        # Launch the browser and create new page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)

        # Click to expand the transcriptions and see the transcriptions
        page.click('xpath=//*[@id="expand"]')
        page.click('xpath=//*[@id="primary-button"]/ytd-button-renderer/yt-button-shape/button')

        # Try to get the transcriptions
        page.wait_for_timeout(5000)
        if (not page.query_selector('xpath=//*[@id="content"]/yt-section-list-renderer')):
            print("Unable to capture the video subtitles. Please try again. If you attempt this more than three times, please be aware that it is not possible to capture the subtitles for this video.")
            return 0

        page.wait_for_selector('xpath=//*[@id="content"]/yt-section-list-renderer')

        i = 1
        while True:
            try:
                # try to get the video time (if user choose yes) and the transcription
                video_time = f"{page.query_selector(f'xpath=//*[@id="contents"]/div[{i}]/macro-markers-panel-item-view-model/timeline-item-view-model/div/transcript-segment-view-model/div[1]').inner_text()}: " if time else ""
                video_transcription = page.query_selector(f'xpath=//*[@id="contents"]/div[{i}]/macro-markers-panel-item-view-model/timeline-item-view-model/div/transcript-segment-view-model/span').inner_text()
                with open("transcript.txt", "a", encoding="utf-8") as f:
                    f.write(f"{video_time}{video_transcription}\n")
                i += 1
            except:
                break

        print("Transcription Complete! See it in the file transcript.txt!")


if __name__ == "__main__":
    try:
        # Ask for URL and time
        URL = input("Paste the URL of the video here:\n>>> ")
        time = input("Did you want time in the file? [y/n]:\n>>> ").lower()
        while time not in ["y", "n"]:
            time = input("See if you type \"y\" or \"n\"!\nDid you want time in the file? [y/n]:\n>>> ").lower()

        time = True if time == "y" else False

        get_transcription(URL, time)  # Call function
    except Exception as e:
        print(f"An error occurred: {e}")
