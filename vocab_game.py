import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# --------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state
# --------------------------------------------------
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# --------------------------------------------------
# 2. ฟังก์ชันเริ่มเกมใหม่
# --------------------------------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# --------------------------------------------------
# 3. ฟังก์ชันแสดงผลลัพธ์
# --------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):

    st.balloons()

    score = 0

    # แปลงคำตอบให้เป็นตัวพิมพ์เล็ก
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # -----------------------------
    # ตรวจข้อ 1
    # -----------------------------
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 1: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{ans1}')"
        )

    # -----------------------------
    # ตรวจข้อ 2
    # -----------------------------
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 2: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{ans2}')"
        )

    # -----------------------------
    # ตรวจข้อ 3
    # -----------------------------
    if u_ans3 == "banana":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 3: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{ans3}')"
        )

    # -----------------------------
    # ตรวจข้อ 4
    # -----------------------------
    # แก้จาก "Cherry" เป็น "cherry"
    if u_ans4 == "cherry":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 4: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{ans4}')"
        )

    # -----------------------------
    # แสดงคะแนน
    # -----------------------------
    st.info(f"🏆 ได้คะแนนรวม: {score}/4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
        st.write("เก่งมาก! คุณตอบถูกทุกข้อ 🥳")
    else:
        st.error("💀 You lose!")
        st.write("ลองใหม่อีกครั้งนะครับ 😊")


# --------------------------------------------------
# 4. ปุ่มเริ่มเกม
# --------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# --------------------------------------------------
# 5. แสดงเวลานับถอยหลัง
# --------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    elapsed_time = time.time() - st.session_state.start
    time_left = max(0, int(30 - elapsed_time))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# --------------------------------------------------
# 6. ช่องกรอกคำตอบ
# --------------------------------------------------
ans1 = st.text_input(
    "ข้อ 1: An a _ _ l e a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
    key="input_ans1"
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat f _ s h. 🐟",
    value=st.session_state.ans2_val,
    key="input_ans2"
)

ans3 = st.text_input(
    "ข้อ 3: Monkeys love to eat b _ n _ n a. 🍌",
    value=st.session_state.ans3_val,
    key="input_ans3"
)

ans4 = st.text_input(
    "ข้อ 4: Ch_ _ _ y is my favorite fruit. 🍒",
    value=st.session_state.ans4_val,
    key="input_ans4"
)


# --------------------------------------------------
# 7. บันทึกคำตอบล่าสุด
# --------------------------------------------------
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# --------------------------------------------------
# 8. ปุ่มส่งคำตอบ
# --------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📤 ส่งคำตอบ"):

        st.session_state.is_ended = True
        st.rerun()

    # ทำให้เวลานับต่อเนื่อง
    time.sleep(1)
    st.rerun()


# --------------------------------------------------
# 9. แสดงผลลัพธ์เมื่อจบเกม
# --------------------------------------------------
if st.session_state.is_ended:

    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )


# --------------------------------------------------
# 10. ข้อมูลผู้จัดทำ
# --------------------------------------------------
st.divider()

st.write(
    "👨‍🎓 นายวรัตม์คล อ้นภากุลวิวัฒน์ "
    "เลขที่ 5 ม.4/17"
)
