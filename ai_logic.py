import random

def du_doan_tai_xiu():
    # Giả lập kết quả của 8 AI (A–H)
    ds_ai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    ket_qua_ai = {ai: random.choice(['Tài', 'Xỉu']) for ai in ds_ai}

    # Tính tỷ lệ
    so_tai = list(ket_qua_ai.values()).count('Tài')
    so_xiu = 8 - so_tai
    phan_tram_tai = round(so_tai / 8 * 100)
    phan_tram_xiu = 100 - phan_tram_tai

    # Kết luận
    ket_luan = "TÀI" if phan_tram_tai > phan_tram_xiu else "XỈU"

    # Kết quả chi tiết
    text = "📈 Kết quả dự đoán từ 8 AI:\n"
    for ai, kq in ket_qua_ai.items():
        text += f"• AI {ai}: {kq}\n"

    text += f"\n📊 Tổng kết:\n- TÀI: {so_tai}/8 ({phan_tram_tai}%)\n- XỈU: {so_xiu}/8 ({phan_tram_xiu}%)"
    text += f"\n\n✅ Kết luận: *{ket_luan}* (tỷ lệ: {max(phan_tram_tai, phan_tram_xiu)}%)"
    return text
