import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from matplotlib import pyplot as plt
import io
import random

TOKEN = "7672832388:AAG7PPAstYq-1g9HX32ltK3IBhY7cBzXy9k"

logging.basicConfig(level=logging.INFO)

# Thuật toán AI demo (8 AI)
def chay_AI(lich_su):
    # Dự đoán ngẫu nhiên thay cho AI thực
    return [random.choice(["tài", "xỉu"]) for _ in range(8)]

def tinh_ty_le(ket_qua):
    tai = ket_qua.count("tài")
    xiu = ket_qua.count("xỉu")
    tong = len(ket_qua)
    return {
        "tài": round(tai / tong * 100),
        "xỉu": round(xiu / tong * 100),
        "chi_tiet": ket_qua
    }

def tao_bieu_do(tai, xiu):
    fig, ax = plt.subplots()
    ax.bar(["TÀI", "XỈU"], [tai, xiu], color=["green", "red"])
    ax.set_ylabel("Tỷ lệ (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Biểu đồ thống kê dự đoán")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return buf

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Gửi lệnh /du_doan để AI phân tích Tài/Xỉu.")

async def du_doan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lich_su = [random.choice(["tài", "xỉu"]) for _ in range(5)]  # lịch sử giả lập
    ket_qua_ai = chay_AI(lich_su)
    ty_le = tinh_ty_le(ket_qua_ai)

    # Kết luận
    ket_luan = "TÀI" if ty_le["tài"] >= ty_le["xỉu"] else "XỈU"
    reply = "📈 *Kết quả AI phân tích:*\n"
    reply += f"- TÀI: {ty_le['tài']}%\n- XỈU: {ty_le['xiu']}%\n\n"
    reply += f"✅ *Kết luận: {ket_luan.upper()} (tỷ lệ: {max(ty_le['tài'], ty_le['xiu'])}%)*\n\n"
    reply += "🤖 *Chi tiết từng AI:*\n"
    for i, kq in enumerate(ty_le["chi_tiet"], 1):
        reply += f"- AI{i}: {kq.upper()}\n"

    # Gửi văn bản
    await update.message.reply_markdown(reply)

    # Gửi ảnh biểu đồ
    buf = tao_bieu_do(ty_le["tài"], ty_le["xiu"])
    await update.message.reply_photo(photo=buf)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("du_doan", du_doan))
    app.run_polling()
