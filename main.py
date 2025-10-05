from playwright.sync_api import sync_playwright


def get_transcription(URL: str, time: bool) -> None:
    with sync_playwright() as p:
        print(f"Coletando transcrição... Aguarde, por favor")

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
                    with open("transcript-v2.txt", "a", encoding="utf-8") as f:
                        f.write(f"{time}: {transcription}\n")
                else:
                    transcription = page.query_selector(f'xpath=//*[@id="segments-container"]/ytd-transcript-segment-renderer[{i}]/div/yt-formatted-string').inner_text()
                    with open("transcript-v2.txt", "a", encoding="utf-8") as f:
                        f.write(f"{transcription}\n")
                i += 1
            except:
                break

        print("Transcrição completa! Veja em transcript.txt!")


if __name__ == "__main__":
    try:
        URL = input("Insira a URL do vídeo do YouTube:\n>>> ")
        time = input("Deseja coletar o tempo também? [s/n]:\n>>> ").lower()
        while time not in ["s", "n"]:
            time = input("Certifique-se que inseriu \"s\" ou \"n\"!\nDeseja coletar o tempo também? [s/n]:\n>>> ").lower()

        time = True if time == "s" else False

        get_transcription(URL, time)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
