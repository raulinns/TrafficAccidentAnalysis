# Dataset 1: Traffic Accidents (2024)
# Pertanyaan Penelitian 1
# Bagaimana hubungan antara jenis cuaca terhadap jumlah korban kecelakaan?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm # Menggunakan statsmodels untuk summary
from sklearn.model_selection import train_test_split
import os # Untuk mendapatkan nama file dari path

# Fungsi untuk melakukan regresi linier dan menampilkan hasilnya
def perform_linear_regression_with_statsmodels(data_frame, weather_col_name, injuries_col_name, csv_filename):
    """
    Melakukan regresi linier menggunakan statsmodels, menampilkan summary,
    dan memvisualisasikan hasil dengan persamaan regresi dan judul yang disesuaikan.
    Asumsi: Kolom cuaca sudah numerik ordinal.

    Args:
        data_frame (pd.DataFrame): DataFrame yang sudah berisi kolom yang relevan.
        weather_col_name (str): Nama kolom untuk deskripsi cuaca (numerik ordinal).
        injuries_col_name (str): Nama kolom untuk jumlah korban.
        csv_filename (str): Nama file CSV untuk judul plot.
    """
    try:
        # 1. Memilih fitur (X) dan target (y)
        X_feature = data_frame[[weather_col_name]] # Variabel independen
        y_target = data_frame[injuries_col_name]    # Variabel dependen

        # Memastikan kolom weather_col_name adalah numerik (sebagai validasi)
        if not pd.api.types.is_numeric_dtype(X_feature[weather_col_name]):
            print(f"Error Kritis: Kolom '{weather_col_name}' diharapkan numerik (karena diasumsikan sudah di-mapping), namun tipe datanya adalah {X_feature[weather_col_name].dtype}.")
            print("Pastikan kolom cuaca di CSV sudah benar-benar numerik ordinal.")
            return
        
        # Memastikan kolom injuries_col_name adalah numerik (sebagai validasi)
        if not pd.api.types.is_numeric_dtype(y_target):
            print(f"Error Kritis: Kolom '{injuries_col_name}' diharapkan numerik, namun tipe datanya adalah {y_target.dtype}.")
            print("Pastikan kolom korban di CSV sudah benar-benar numerik.")
            return


        # Menghapus baris dengan nilai NaN pada kolom yang digunakan
        combined_data = pd.concat([X_feature, y_target], axis=1)
        combined_data.dropna(subset=[weather_col_name, injuries_col_name], inplace=True)
        
        if combined_data.empty:
            print("Error Kritis: Tidak ada data valid tersisa setelah menghapus NaN dari kolom yang digunakan.")
            return
            
        X_processed = combined_data[[weather_col_name]]
        y_processed = combined_data[injuries_col_name]

        # 2. Membagi data
        X_train, X_test, y_train, y_test = train_test_split(X_processed, y_processed, test_size=0.2, random_state=42)

        if X_train.empty or y_train.empty or X_test.empty or y_test.empty:
            print("Error Kritis: Data latih atau data uji kosong setelah pembagian. Ini bisa terjadi jika dataset terlalu kecil atau banyak NaN.")
            return

        # 3. Menambahkan konstanta (intercept)
        X_train_sm = sm.add_constant(X_train)
        X_test_sm = sm.add_constant(X_test)

        # 4. Membuat dan melatih model OLS
        model = sm.OLS(y_train, X_train_sm)
        results = model.fit()

        # 5. Menampilkan rekap hasil regresi
        print("\n--- Rekap Hasil Regresi Linier (statsmodels OLS) ---")
        print(results.summary())
        print("------------------------------------------------------\n")

        # 6. Mendapatkan koefisien
        intercept = results.params['const']
        if weather_col_name not in results.params:
            print(f"Error: Kolom '{weather_col_name}' tidak ditemukan di parameter model. Parameter yang ada: {results.params.index.tolist()}")
            return
        slope = results.params[weather_col_name]
        r_squared = results.rsquared

        # 7. Membuat prediksi
        y_pred = results.predict(X_test_sm)

        # 8. Visualisasi hasil
        plt.figure(figsize=(12, 7))
        plt.scatter(X_test[weather_col_name], y_test, color='blue', label='Data Aktual', alpha=0.6)
        
        sort_axis = np.argsort(X_test[weather_col_name].values.flatten())
        plt.plot(X_test[weather_col_name].values[sort_axis], y_pred.values[sort_axis], color='red', linewidth=2, label='Garis Regresi')
        
        plt.title(f'Regresi Linear Dataset 1: "{csv_filename}"', fontsize=15)
        plt.xlabel(f"{weather_col_name} (Ordinal)", fontsize=12)
        plt.ylabel(injuries_col_name, fontsize=12)
        
        equation_text = f'{injuries_col_name} $\\approx$ {slope:.2f} $\\times$ {weather_col_name} + {intercept:.2f}\n$R^2 = {r_squared:.2f}$'
        plt.text(0.05, 0.95, equation_text, transform=plt.gca().transAxes, fontsize=12,
                 verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', fc='wheat', alpha=0.5))
        
        # Menampilkan semua nilai unik pada sumbu X (waktu kejadian)
        unique_x_values = sorted(X_processed[weather_col_name].unique())
        plt.xticks(unique_x_values)

        # Menampilkan ticks pada sumbu Y yang sesuai dengan range data
        y_min, y_max = int(y_processed.min()), int(y_processed.max())
        y_step = max(1, (y_max - y_min) // 20)  # Maksimal 20 ticks untuk keterbacaan
        plt.yticks(range(y_min, y_max + 1, y_step))

        # Menambahkan label untuk sumbu X
        plt.xlabel(weather_col_name, fontsize=12)

        plt.legend(loc='lower right')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'../../doc/data-analytic/DS1-Pertanyaan1.png', dpi=300, bbox_inches='tight')
        plt.show()

    except Exception as e:
        print(f"Terjadi error dalam fungsi perform_linear_regression_with_statsmodels: {e}")
        import traceback
        traceback.print_exc()

# --- Cara Penggunaan ---
if __name__ == "__main__":
    file_path = '../../dataset/transformasi-dataset/traffic_accidents_2024_mapped.csv'
    actual_filename = os.path.basename(file_path)
    jenis_cuaca = "weather_condition" 
    jumlah_korban = "injuries_total"

    try:
        data_full = pd.read_csv(file_path)

        if jenis_cuaca not in data_full.columns or jumlah_korban not in data_full.columns:
            print(f"Error Kritis: Kolom '{jenis_cuaca}' atau '{jumlah_korban}' tidak ditemukan di CSV '{file_path}'.")
            print(f"Kolom yang tersedia: {data_full.columns.tolist()}")
            exit()
            
        data_selected = data_full[[jenis_cuaca, jumlah_korban]].copy()

        perform_linear_regression_with_statsmodels(data_selected, jenis_cuaca, jumlah_korban, actual_filename)

    except FileNotFoundError:
        print(f"CRITICAL ERROR: File CSV '{file_path}' tidak ditemukan. Pastikan path dan nama file sudah benar.")
    except KeyError as e:
        # Error ini seharusnya tidak terjadi jika pengecekan kolom di atas sudah berjalan
        print(f"CRITICAL ERROR: Kolom '{e}' tidak ditemukan saat seleksi. Ini tidak seharusnya terjadi jika nama kolom sudah divalidasi.")
    except Exception as e:
        print(f"Terjadi error umum: {e}")
        import traceback
        traceback.print_exc()