// メッセージボックスを閉じる関数をアニメーション付きで更新
function closeMessage() {
    var messageBox = document.getElementById('message-box');
    messageBox.classList.add('hidden'); // フェードアウトアニメーションを適用
    setTimeout(function() {
        messageBox.style.display = 'none';
    }, 1000); // アニメーションが完了した後に要素を非表示にする
}
function closeWindow() {
    window.close();
}
