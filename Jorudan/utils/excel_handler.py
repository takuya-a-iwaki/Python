import os
import tkinter as tk
from tkinter import filedialog, messagebox
from openpyxl import load_workbook

def select_excel_file():
    root = tk.Tk()
    root.withdraw()  # GUIを非表示にする
    file_path = filedialog.askopenfilename(
        title="エクセルファイルを選択してください",
        filetypes=[("Excel files", "*.xlsm")]
    )
    if not file_path:
        messagebox.showerror("エラー", "ファイルが選択されていません。")
        return None

    # ファイル名のバリデーション
    if "赴任等旅費請求内訳書兼領収書" not in os.path.basename(file_path):
        messagebox.showerror("エラー", "指定されたファイル名が正しくありません。")
        return None

    return file_path

def read_excel_data(file_path):
    try:
        wb = load_workbook(file_path, data_only=True)
        sheet = wb["基本情報（情報連携シート）"]

        data = {
            "新在勤庁最寄り駅": sheet["Q18"].value,
            "新自宅住所最寄り駅": sheet["Q21"].value,
            "旧在勤庁最寄り駅": sheet["Q33"].value,
            "旧自宅住所最寄り駅": sheet["Q36"].value,
            "職員番号": sheet["C9"].value,
            "職員氏名": sheet["G9"].value,
        }
        wb.close()
        return data
    except Exception as e:
        messagebox.showerror("エラー", f"エクセルファイルの読み込み中にエラーが発生しました: {e}")
        return None