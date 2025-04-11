from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from datetime import datetime
import os
import configparser  # 設定ファイルを読み込むためのモジュール
import base64  # Base64 デコード用
import sys  # 実行ファイルのパスを取得するために使用

def get_base_path():
    """実行ファイルのベースパスを取得"""
    if getattr(sys, 'frozen', False):
        # PyInstaller でビルドされた場合
        return os.path.dirname(sys.executable)  # 実行ファイルのディレクトリを返す
    else:
        # 通常のスクリプト実行時
        current_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.abspath(os.path.join(current_path, ".."))  # utils の親ディレクトリを返す

def setup_browser():
    # 設定ファイルのパスを取得
    base_path = get_base_path()
    config_path = os.path.join(base_path, "config.ini")  # Jorudan 配下の config.ini を指定

    # 設定ファイルを読み込む
    config = configparser.ConfigParser()
    if not config.read(config_path):
        raise FileNotFoundError(f"設定ファイルが見つかりません: {config_path}")

    # Edge WebDriver のパスを取得
    try:
        driver_path = config["webdriver"]["edge_driver_path"]
    except KeyError:
        raise KeyError("config.ini に [webdriver] セクションまたは edge_driver_path キーが見つかりません。")

    # Edge オプションを設定
    options = Options()
    options.use_chromium = True  # ChromiumベースのEdgeを使用する
    options.add_argument("--headless")  # ヘッドレスモードを有効化
    options.add_argument("--disable-gpu")  # GPUを無効化

    # Edge WebDriver を初期化
    service = EdgeService(driver_path)
    browser = webdriver.Edge(service=service, options=options)
    return browser

def search_route(browser, departure, arrival, output_dir, staff_id, staff_name, pattern_label):
    try:
        browser.get("https://www.jorudan.co.jp/norikae/")
        browser.find_element(By.ID, "eki1_in").send_keys(departure)
        browser.find_element(By.ID, "eki2_in").send_keys(arrival)
        
        # 検索ボタンを JavaScript で直接クリック
        search_button = browser.find_element(By.CLASS_NAME, "btn.search")
        browser.execute_script("arguments[0].click();", search_button)

        # 検索結果が表示されるまで待機（必要に応じて明示的な待機を追加）
        browser.implicitly_wait(5)

        # PDF ファイルの保存パスを設定
        pdf_path = os.path.join(output_dir, f"{staff_id}_{staff_name}_{pattern_label}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf")

        # Web ページ全体を PDF として保存
        print_options = {
            "landscape": False,
            "displayHeaderFooter": False,
            "printBackground": True,
            "preferCSSPageSize": True
        }
        pdf_data = browser.execute_cdp_cmd("Page.printToPDF", print_options)

        # PDF データをデコードしてファイルに書き込む
        with open(pdf_path, "wb") as pdf_file:
            pdf_file.write(base64.b64decode(pdf_data["data"]))

        return pdf_path
    except Exception as e:
        print(f"検索中にエラーが発生しました: {e}")
        return None