import streamlit as st
st.title("⏱️ เกมเติมศัพท์จับเวลา")
# 1. กำหนดค่าเริ่มต้นใน session_state
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
# ฟังก์ชันเริ่มเกมใหม่
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False
# ----------------------------------------------------
# ฟังก์ชันแสดงผลคะแนน
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0
    answers = [
        (ans1, "apple"),
        (ans2, "fish"),
        (ans3, "banana"),
        (ans4, "lemon")
    ]
    for i, (answer, correct) in enumerate(answers, start=1):
        user_answer = answer.strip().lower()
        if user_answer == correct:
            st.success(f"✅ ข้อ {i}: ถูกต้อง")
            score += 1
        else:
            st.error(f"❌ ข้อ {i}: ไม่ถูกต้อง")
    st.info(f"🏆 ได้คะแนนรวม: {score}/4 คะแนน")
    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")
# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)
# ----------------------------------------------------
# 2. แสดงเวลานับถอยหลัง
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()
st.divider()
# ----------------------------------------------------
# 3. ช่องรับคำตอบ
# ----------------------------------------------------
ans1 = st.text_input(
    "ข้อ 1: 🍎 `a _ p l e`",
    value=st.session_state.ans1_val
)
ans2 = st.text_input(
    "ข้อ 2: 🐟 `f _ s h`",
    value=st.session_state.ans2_val
)
ans3 = st.text_input(
    "ข้อ 3: 🍌 `b _ n _ n _`",
    value=st.session_state.ans3_val
)
ans4 = st.text_input(
    "ข้อ 4: 🍋 `l _ m _ n`",
    value=st.session_state.ans4_val
)
# อัปเดตค่าล่าสุด
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
# ----------------------------------------------------
# 4. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()
    time.sleep(1)
    st.rerun()
# ----------------------------------------------------
# 5. แสดง Dialog ผลลัพธ์
# ----------------------------------------------------
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)
st.divider()
st.write("นายวรัตม์คล อ้นภากุลวิวัฒน์ เลขที่5 ม.4/17")
```
 ตอนนี้โจทย์จะแสดงแค่ **คำศัพท์ + ช่องว่าง** เช่น `b _ n _ n _` ไม่มีประโยคหรือวลีแล้วครับ
st.divider()
st.write("นายวรัตม์คล อ้นภากุลวิวัฒน์ เลขที่5 ม.4/17")
