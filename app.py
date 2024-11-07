from flask import Flask, request, render_template, send_from_directory
from datetime import datetime
import csv
import os

app = Flask(__name__)


@app.route('/track')
def track_user():
    # ユーザーIDを取得、未知の場合は'Unknown'を設定
    user_id = request.args.get('user_id', 'Unknown')

    # ログファイル名を指定
    log_filename = "access_log.csv"

    # ログファイルがまだ存在しない場合は、ヘッダーと共に新規作成
    if not os.path.exists(log_filename):
        with open(log_filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["User ID", "Timestamp", "User Agent", "IP Address"])

    # ログファイルにアクセスデータを追記
    with open(log_filename, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            user_id,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            request.user_agent.string,
            request.remote_addr
        ])

    return render_template('welcome.html', user_id=user_id)


@app.route('/download-logs')
def download_logs():
    try:
        # 現在の作業ディレクトリを取得
        directory = os.getcwd()
        # ログファイルをダウンロードとして提供
        return send_from_directory(directory, 'access_log.csv', as_attachment=True)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
