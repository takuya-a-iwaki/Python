from utils.excel_handler import select_excel_file, read_excel_data
from utils.browser_handler import setup_browser, search_route
import os
import tkinter as tk
from tkinter import messagebox

def main():
    # エクセルファイル選択
    file_path = select_excel_file()
    if not file_path:
        return

    # データ読み込み
    data = read_excel_data(file_path)
    if not data:
        return

    # 出力ディレクトリ
    output_dir = os.path.dirname(file_path)

    # ブラウザセットアップ
    browser = setup_browser()

    # 検索パターン
    patterns = [
        (data["旧在勤庁最寄り駅"], data["新在勤庁最寄り駅"], "在在"),
        (data["旧在勤庁最寄り駅"], data["新自宅住所最寄り駅"], "在自"),
        (data["旧自宅住所最寄り駅"], data["新自宅住所最寄り駅"], "自自"),
        (data["旧自宅住所最寄り駅"], data["新在勤庁最寄り駅"], "自在"),
    ]

    # GUI ウィンドウを作成
    root = tk.Tk()
    root.title("進捗状況")
    root.geometry("400x100")

    # 固定メッセージを表示
    progress_label = tk.Label(root, text="検索処理を実行中です。しばらくお待ちください...")
    progress_label.pack(pady=20)

    # GUI を更新して表示
    root.update()

    # 各パターンで検索を実行
    for count, (departure, arrival, pattern_label) in enumerate(patterns, start=1):
        pdf_path = search_route(browser, departure, arrival, output_dir, data["職員番号"], data["職員氏名"], pattern_label)
        if pdf_path:
            print(f"PDF保存完了: {pdf_path}")

    # ブラウザを閉じる
    browser.quit()

    # 処理終了時にメッセージダイアログを表示
    messagebox.showinfo("完了", "すべての検索が完了しました！")
    root.destroy()  # ウィンドウを閉じる

if __name__ == "__main__":
    main()