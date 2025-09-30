from playwright.sync_api import sync_playwright


def get_transcription(URL):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)

        print(f"Coletando transcrição... Aguarde, por favor")

        # Entrando na transcrição
        page.click('xpath=//*[@id="expand"]')
        page.click('xpath=//*[@id="primary-button"]/ytd-button-renderer/yt-button-shape/button')

        page.wait_for_selector('xpath=//*[@id="body"]/ytd-transcript-segment-list-renderer')

        # Colentando todo o texto e inserindo em transcript.txt
        transcription = page.query_selector('xpath=//*[@id="body"]/ytd-transcript-segment-list-renderer').inner_text()
        with open("transcript.txt", "w", encoding="utf-8") as f:
            f.write(transcription)

        print("Transcrição completa! Veja em transcript.txt!")


if __name__ == "__main__":
    try:
        URL = input("Insira a URL do vídeo do YouTube: ")
        get_transcription(URL)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
