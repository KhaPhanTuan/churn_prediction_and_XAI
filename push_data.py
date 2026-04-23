import pandas as pd
import os
import urllib.parse  # Thêm thư viện này để xử lý mật khẩu có ký tự lạ
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# 1. Lấy thông tin và xử lý mật khẩu (Tránh lỗi ký tự đặc biệt)
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = urllib.parse.quote_plus(os.getenv('DB_PASSWORD')) # QUAN TRỌNG: Mã hóa mật khẩu
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME') # Hãy thử để 'defaultdb' trước

# 2. Tạo URL kết nối chuẩn
db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 3. Cấu hình Engine với SSL "mạnh" hơn cho Aiven
engine = create_engine(
    db_url,
    connect_args={
        "ssl": {
            "ssl_mode": "REQUIRED" # Ép dùng SSL
        }
    }
)

# 4. Danh sách các bảng cần đẩy
# Lưu ý: Sửa lại đường dẫn file CSV trên máy ông cho đúng
tasks = [
    ('dataset/customers.csv', 'customers'),
    ('dataset/contracts.csv', 'contracts'),
    ('dataset/churn_records.csv', 'churn_records'),
    ('dataset/internet_services.csv', 'internet_services'),
    ('dataset/payment_methods.csv', 'payment_methods'),
    ('dataset/phone_services.csv', 'phone_services'),
    ('dataset/user.csv', 'user'), # Bảng user của ông
]

def push_data():
    try:
        print(f"--- Đang thử kết nối tới {DB_HOST} ---")
        with engine.connect() as conn:
            print("✅ KẾT NỐI AIVEN THÀNH CÔNG RỒI KHA ƠI!")
            
            for file_path, table_name in tasks:
                if os.path.exists(file_path):
                    df = pd.read_csv(file_path)
                    print(f"🚀 Đang đẩy dữ liệu vào bảng: {table_name}...")
                    df.to_sql(table_name, con=engine, if_exists='append', index=False)
                    print(f"✔️ Xong bảng {table_name}")
                else:
                    print(f"❌ Không thấy file: {file_path}")
    except Exception as e:
        print(f"💥 Vẫn bị từ chối: {e}")
        print("\n💡 Gợi ý cho Kha: Thử vào file .env đổi DB_NAME thành 'defaultdb' xem sao!")

if __name__ == "__main__":
    push_data()