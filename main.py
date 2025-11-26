from playwright.sync_api import sync_playwright


def get_transcription(URL: str, time: bool) -> None:
    with sync_playwright() as p:
        print(f"Getting transcription... Please be patient and wait!")

        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL)

        page.click('xpath=//*[@id="expand"]')
        page.click('xpath=//*[@id="primary-button"]/ytd-button-renderer/yt-button-shape/button')

        page.wait_for_selector('xpath=//*[@id="segments-container"]/ytd-transcript-segment-renderer[1]/div/yt-formatted-string')

        i = 1
        while True:
            try:
                if time:
                    time = page.query_selector(f'xpath=//*[@id="segments-container"]/ytd-transcript-segment-renderer[{i}]/div/div/div').inner_text()
                    transcription = page.query_selector(f'xpath=//*[@id="segments-container"]/ytd-transcript-segment-renderer[{i}]/div/yt-formatted-string').inner_text()
                    with open("transcript.txt", "a", encoding="utf-8") as f:
                        f.write(f"{time}: {transcription}\n")
                else:
                    transcription = page.query_selector(f'xpath=//*[@id="segments-container"]/ytd-transcript-segment-renderer[{i}]/div/yt-formatted-string').inner_text()
                    with open("transcript.txt", "a", encoding="utf-8") as f:
                        f.write(f"{transcription}\n")
                i += 1
            except:
                break

        print("Transcription Complete! See it in the file transcript.txt!")


if __name__ == "__main__":
    try:
        URL = input("Paste the URL of the video here:\n>>> ")
        time = input("Did you want time in the file? [y/n]:\n>>> ").lower()
        while time not in ["s", "n"]:
            time = input("See if you type \"y\" or \"n\"!\nDid you want time in the file? [y/n]:\n>>> ").lower()

        time = True if time == "y" else False

        get_transcription(URL, time)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
