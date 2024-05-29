import re
import tkinter as tk
from tkinter import scrolledtext
from fuzzywuzzy import fuzz

# Data kelas dan tugas
kelas = {
    "pendidikan pancasila": {
        "tugas": {
            "tugas pemilu": {
                "deskripsi": "Silahkan baca petunjuk terlampir\nKetentuan tugas:\n- Tugas terakhir dikumpulkan tanggal 15 Februari 2024 15:00 WIB\n- Tugas dikumpulkan melalui situs e-class dengan mengirimkan file\n- Tugas tidak bisa dikumpul ulang\n- Tugas masih bisa dikumpulkan setelah tanggal berakhir dengan resiko pengurangan nilai",
                "deadline": "15 Februari 2024",
            },
            "tm 6 sebagai pendidikan pancasila": {
                "deskripsi": "Diskusikan pentingnya Pancasila dalam kehidupan berbangsa dan bernegara.",
                "deadline": "20 Maret 2024",
            },
            "uts": {
                "deskripsi": "Ujian Tengah Semester untuk Pendidikan Pancasila.",
                "deadline": "10 April 2024",
            },
            "tugas kelompok sila 1": {
                "deskripsi": "Presentasi mengenai Sila Pertama Pancasila.",
                "deadline": "5 Mei 2024",
            },
            "tugas kelompok sila kedua": {
                "deskripsi": "Analisis penerapan Sila Kedua dalam masyarakat.",
                "deadline": "12 Mei 2024",
            },
            "tugas kelompok sila ketiga": {
                "deskripsi": "Makalah tentang pentingnya persatuan dalam Sila Ketiga.",
                "deadline": "19 Mei 2024",
            },
            "pr kelompok": {
                "deskripsi": "Pekerjaan rumah mengenai materi yang dibahas minggu ini.",
                "deadline": "26 Mei 2024",
            },
            "tugas kelompok sila 4": {
                "deskripsi": "Diskusi kelompok tentang penerapan demokrasi dalam Sila Keempat.",
                "deadline": "2 Juni 2024",
            }
        }
    },
    "pemrograman web": {
        "tugas": {
            "tugas aktivitas kelas 1": {
                "deskripsi": "Buat halaman web statis menggunakan HTML dan CSS.",
                "deadline": "25 Februari 2024",
            },
            "tugas 2": {
                "deskripsi": "Implementasi JavaScript untuk interaktifitas pada halaman web.",
                "deadline": "5 Maret 2024",
            },
            "midterm project": {
                "deskripsi": "Proyek tengah semester yang mencakup penggunaan HTML, CSS, dan JavaScript.",
                "deadline": "20 Maret 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir semester berupa aplikasi web sederhana.",
                "deadline": "15 Mei 2024",
            }
        }
    },
    "praktikum pemrograman web": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Instalasi dan konfigurasi server web lokal.",
                "deadline": "28 Februari 2024",
            },
            "tugas 2": {
                "deskripsi": "Membuat halaman web dengan backend sederhana menggunakan PHP.",
                "deadline": "10 Maret 2024",
            },
            "tugas 3": {
                "deskripsi": "Koneksi database MySQL dengan PHP.",
                "deadline": "25 Maret 2024",
            }
        }
    },
    "kecerdasan buatan": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Membuat program sederhana yang menerapkan algoritma pencarian.",
                "deadline": "1 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Implementasi jaringan saraf tiruan untuk klasifikasi data.",
                "deadline": "15 Maret 2024",
            },
            "project akhir": {
                "deskripsi": "Proyek akhir mengenai aplikasi kecerdasan buatan dalam kehidupan nyata.",
                "deadline": "20 Mei 2024",
            }
        }
    },
    "keamanan komputer": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Analisis serangan malware dan cara pencegahannya.",
                "deadline": "5 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Implementasi firewall dan IDS untuk proteksi jaringan.",
                "deadline": "20 Maret 2024",
            },
            "final exam": {
                "deskripsi": "Ujian akhir mengenai topik-topik keamanan komputer.",
                "deadline": "30 Mei 2024",
            }
        }
    },
    "etika profesi teknologi informasi": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Makalah tentang etika dalam penggunaan data pribadi.",
                "deadline": "10 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Presentasi tentang kode etik profesi di bidang TI.",
                "deadline": "25 Maret 2024",
            },
            "project kelompok": {
                "deskripsi": "Proyek kelompok mengenai kasus etika dalam teknologi informasi.",
                "deadline": "10 Mei 2024",
            }
        }
    },
    "rekayasa perangkat lunak beriorientasi obyek": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Implementasi dasar OOP dalam bahasa pemrograman pilihan.",
                "deadline": "12 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Desain dan implementasi pola desain dalam proyek kecil.",
                "deadline": "25 Maret 2024",
            },
            "tugas akhir": {
                "deskripsi": "Proyek akhir yang mencakup seluruh konsep OOP yang dipelajari.",
                "deadline": "5 Mei 2024",
            }
        }
    },
    "praktikum rekayasa perangkat lunak beriorientasi obyek": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Praktikum dasar-dasar OOP.",
                "deadline": "15 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Praktikum implementasi pola desain.",
                "deadline": "30 Maret 2024",
            },
            "proyek praktikum": {
                "deskripsi": "Proyek praktikum akhir semester.",
                "deadline": "20 Mei 2024",
            }
        }
    },
    "data warehouse": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Desain skema data warehouse untuk perusahaan retail.",
                "deadline": "20 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Implementasi ETL process untuk data warehouse.",
                "deadline": "10 April 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir berupa implementasi data warehouse lengkap.",
                "deadline": "25 Mei 2024",
            }
        }
    },
    "sistem informasi geografis": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Pemetaan data menggunakan software GIS.",
                "deadline": "12 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Analisis data spasial untuk kasus studi tertentu.",
                "deadline": "25 Maret 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir berupa analisis dan visualisasi data geografis.",
                "deadline": "5 Mei 2024",
            }
        }
    },
    "machine learning": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Implementasi model regresi linear sederhana.",
                "deadline": "15 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Klasifikasi data menggunakan algoritma KNN.",
                "deadline": "30 Maret 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir berupa aplikasi machine learning untuk kasus nyata.",
                "deadline": "20 Mei 2024",
            }
        }
    },
    "big data": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Pengolahan data besar menggunakan Hadoop.",
                "deadline": "10 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Analisis data besar menggunakan Apache Spark.",
                "deadline": "25 Maret 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir berupa analisis big data untuk kasus bisnis tertentu.",
                "deadline": "15 Mei 2024",
            }
        }
    },
    
    "matematika": {
        "tugas": {
            
        }
    }
}

# Patterns untuk AI chatbot
patterns = {
    r"(?:apa saja|sebutkan|daftar) semua tugas(?: tanpa detail)? berdasarkan kelas(?:nya)?": lambda _: get_all_tugas_by_kelas(),
    r"(?:apa saja|sebutkan|daftar) kelas(?: yang)? ada": lambda _: get_kelas_list(),
    r"(?:apa saja|sebutkan|daftar|apa) kelas?": lambda _: get_kelas_list(),
    r"(?:apa saja|sebutkan|daftar) kelas(?: yang)? tersedia": lambda _: get_kelas_list(),
    r"(?:apa saja|sebutkan|daftar|apa) (?:tugas|PR)(?: untuk| di)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"(?:apa saja|sebutkan|daftar) semua tugas(?: yang ada)?": lambda _: get_all_tugas_detail(),
    r"(?:info|ditel) (?:tugas )?(.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:ditel) (?:tugas )?(.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:ditel) (?:tugas )?(.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:apa ditel) tugas (.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:apa saja|sebutkan|daftar) semua tugas(?: beserta ditel-nya)?": lambda _: get_all_tugas_detail(),
    r"deskripsi tugas (.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"deadline tugas (.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"kelas apa saja yang tersedia?": lambda _: get_kelas_list(),
    r"kelas saya?": lambda _: get_kelas_list(),
    r"kelasku?": lambda _: get_kelas_list(),
    r"info kelas?": lambda _: get_kelas_list(),
    r"daftar kelas yang bisa diambil": lambda _: get_kelas_list(),
    r"tolong beri info tugas untuk kelas (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"bisa kasih tahu semua tugas yang ada?": lambda _: get_all_tugas_detail(),
    r"apa saja tugas yang ada beserta ditel-nya?": lambda _: get_all_tugas_detail(),
    r"ceritakan tentang tugas (.*) di kelas (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"apa deadline dari tugas (.*) di kelas (.*)?": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"ditel tugas (.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"kelas?": lambda _: get_kelas_list(),
    r"daftar tugas": lambda _: get_all_tugas_detail(),
    r"ditel tugas nomor (\d+) kelas (.*)": lambda matches: get_tugas_detail_by_index(matches[1].strip().lower(), int(matches[0]) - 1),
    r"ditel tugas nomor (\d+)": lambda matches: get_tugas_detail_by_index(last_class_requested, int(matches[0]) - 1),
    r"nomor (\d+)": lambda matches: get_tugas_detail_by_index(last_class_requested, int(matches[0]) - 1),
    r"(?:apa saja|sebutkan|daftar|apa) (?:tugas|PR)(?: untuk| di)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"(?:info|ditel) tugas (.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:info|ditel) tugas (.*)": lambda matches: get_tugas_detail(last_class_requested, matches[0].strip().lower()),
    r"(?:apa) tugas (.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:apa) tugas (.*)": lambda matches: get_tugas_detail(last_class_requested, matches[0].strip().lower()),
    r"(?:info|ditel) tugas (.*) (?:apa)": lambda matches: get_tugas_detail(last_class_requested, matches[0].strip().lower()),
    r"tugas (.*)": lambda matches: get_tugas_detail(last_class_requested, matches[0].strip().lower()),
    r"(?:apa saja|sebutkan|daftar) semua tugas(?: beserta deadline-nya)?": lambda _: get_all_tugas_detail(),
    r"deadline tugas (.*) di (.*)": lambda matches: get_deadline(matches[1].strip().lower(), matches[0].strip().lower()),
}

kelas_sinonim = {
    "apa saja": ["sebutkan", "daftar", "apa sih", "kasih tau","mau liat","mau lihat"],
    "tugas" : ["PR","tgs"],
    "ditel" : ["detail","deskripsi","ceritakan","info","informasi","cerita","jelaskan","jelasin"],
    "kelas": ["matkul","MATKUL", "mata kuliah", "pelajaran","kls"],
    "tersedia": ["ada", "yang bisa diambil", "tersedia saat ini"],
    "tugas": ["pekerjaan", "tugas kuliah", "tugas akademik"],
    "deadline": ["batas waktu", "waktu pengumpulan"],
    "deskripsi": ["uraian", "penjelasan", "keterangan"],
    "pengolahan data besar": ["proses data besar", "manipulasi data besar"],
    "pendidikan pancasila":["pp"],
    "pemrograman web":["progweb"],
    "praktikum pemrograman web":["prakprogweb"],
    "rekayasa perangkat lunak beriorientasi obyek":["rpl","rplbo"],
    "praktikum rekayasa perangkat lunak beriorientasi obyek":["prakrplbo","prakrpl"], 
    "kecerdasan buatan":["ai"],
    "keamanan komputer":["kakom"],
    "etika profesi teknologi informasi":["etprof"],
    "data warehouse":["dw"],
    "daftar" : ["list"],
    "nomor" : ["no"],
}

last_class_requested = None

def get_deadline(kelas_name, tugas_name):
    if kelas_name in kelas:
        tugas_list = kelas[kelas_name]["tugas"]
        if tugas_name in tugas_list:
            deadline = tugas_list[tugas_name].get("deadline", "Deadline tidak tersedia.")
            return f"Deadline untuk tugas '{tugas_name}' di kelas '{kelas_name}' adalah: {deadline}"
        else:
            return f"Tugas '{tugas_name}' tidak ditemukan di kelas '{kelas_name}'."
    else:
        return "Nama kelas tidak ditemukan. Tolong periksa dan ulangi lagi."


def get_all_tugas_by_kelas():
    all_tugas_by_kelas = {kelas_name: [] for kelas_name in kelas}
    for kelas_name, kelas_info in kelas.items():
        tugas_list = kelas_info.get("tugas", {})
        for tugas_name in tugas_list:
            all_tugas_by_kelas[kelas_name].append(tugas_name)
    return "\n".join([f"{kelas_name}:\n" + "\n".join(f"- {tugas}" for tugas in tugas_list) for kelas_name, tugas_list in all_tugas_by_kelas.items()])

# Fungsi untuk mendapatkan daftar kelas
def get_kelas_list():
    kelas_list = "\n".join(kelas.keys())
    return f"Berikut adalah daftar kelas yang Anda ambil:\n{kelas_list}"

# Fungsi untuk mendapatkan daftar tugas untuk kelas tertentu
def get_tugas(kelas_name):
    if kelas_name in kelas:
        tugas_list = kelas[kelas_name]["tugas"]
        tugas_str = "\n".join(f"{i+1}. {tugas}" for i, tugas in enumerate(tugas_list))
        return f"Berikut adalah daftar tugas untuk {kelas_name}:\n{tugas_str}\n\nSilahkan pilih nomor tugas untuk melihat detailnya.\nContoh: 'nomor 1'"
    else:
        return "Tolong ulangi pertanyaan dan sertakan nama kelas."

# Fungsi untuk mendapatkan detail tugas tertentu di kelas tertentu
def get_tugas_detail_by_index(kelas_name, index):
    if kelas_name in kelas:
        tugas_list = kelas[kelas_name]["tugas"]
        if 0 <= index < len(tugas_list):
            tugas_name = list(tugas_list.keys())[index]
            tugas = tugas_list[tugas_name]
            deskripsi = tugas.get("deskripsi", "Deskripsi tidak tersedia.")
            deadline = tugas.get("deadline", "Deadline tidak tersedia.")
            return f"Detail untuk tugas {tugas_name} di kelas {kelas_name}:\nDeskripsi: {deskripsi}\nDeadline: {deadline}"
        else:
            return "Nomor tugas tidak valid."
    else:
        return "Tolong ulangi pertanyaan dan sertakan nama kelas."

# Fungsi untuk mendapatkan detail tugas tertentu di kelas tertentu
def get_tugas_detail(kelas_name, tugas_name):
    if kelas_name in kelas:
        tugas_list = kelas[kelas_name]["tugas"]
        if tugas_name in tugas_list:
            tugas = tugas_list[tugas_name]
            deskripsi = tugas.get("deskripsi", "Deskripsi tidak tersedia.")
            deadline = tugas.get("deadline", "Deadline tidak tersedia.")
            return f"Detail untuk tugas {tugas_name} di kelas {kelas_name}:\nDeskripsi: {deskripsi}\nDeadline: {deadline}"
        else:
            return f"Tugas {tugas_name} tidak ditemukan di kelas {kelas_name}."
    else:
        return "Tolong ulangi pertanyaan dan sertakan nama kelas."

# Fungsi untuk mendapatkan daftar semua tugas
def get_all_tugas():
    all_tugas = []
    for kelas_name, kelas_info in kelas.items():
        tugas_list = kelas_info.get("tugas", {})
        for tugas_name, tugas_detail in tugas_list.items():
            all_tugas.append(f"{tugas_name} ({kelas_name}) - Deadline: {tugas_detail.get('deadline', 'Tidak tersedia')}")
    if all_tugas:
        return "Berikut adalah daftar semua tugas yang ada:\n" + "\n".join(all_tugas)
    else:
        return "Tidak ada tugas yang tersedia saat ini."

# Fungsi untuk mendapatkan detail semua tugas beserta deadlinenya
def get_all_tugas_detail():
    all_tugas_detail = []
    for kelas_name, kelas_info in kelas.items():
        tugas_list = kelas_info.get("tugas", {})
        if tugas_list:
            all_tugas_detail.append(f"Kelas: {kelas_name}")
            for tugas_name, tugas_detail in tugas_list.items():
                deskripsi = tugas_detail.get("deskripsi", "Deskripsi tidak tersedia.")
                deadline = tugas_detail.get("deadline", "Deadline tidak tersedia.")
                all_tugas_detail.append(f"  - Tugas: {tugas_name}")
                all_tugas_detail.append(f"    Deskripsi: {deskripsi}")
                all_tugas_detail.append(f"    Deadline: {deadline}")
    if all_tugas_detail:
        return "\n".join(all_tugas_detail)
    else:
        return "Tidak ada tugas yang tersedia saat ini."

# Fungsi untuk mendapatkan daftar kelas yang tersedia
def get_kelas_list():
    kelas_list = "\n".join(kelas.keys())
    return f"Berikut adalah daftar kelas yang Anda ambil:\n{kelas_list}"

# Fungsi untuk mendapatkan daftar tugas untuk kelas tertentu
def get_tugas_detail(kelas_name, tugas_name):
    if kelas_name in kelas:
        tugas_list = kelas[kelas_name]["tugas"]
        if tugas_name in tugas_list:
            tugas = tugas_list[tugas_name]
            deskripsi = tugas.get("deskripsi", "Deskripsi tidak tersedia.")
            deadline = tugas.get("deadline", "Deadline tidak tersedia.")
            return f"Detail untuk tugas {tugas_name} di kelas {kelas_name}:\nDeskripsi: {deskripsi}\nDeadline: {deadline}"
        else:
            # Pencarian string parsial
            max_similarity = -1
            matching_tugas = None
            for existing_tugas_name in tugas_list:
                similarity = fuzz.partial_ratio(tugas_name, existing_tugas_name)
                if similarity > max_similarity:
                    max_similarity = similarity
                    matching_tugas = existing_tugas_name

            if max_similarity > 70:  # Ambil jika kesamaan cukup tinggi
                tugas = tugas_list[matching_tugas]
                deskripsi = tugas.get("deskripsi", "Deskripsi tidak tersedia.")
                deadline = tugas.get("deadline", "Deadline tidak tersedia.")
                return f"Detail untuk tugas {matching_tugas} di kelas {kelas_name}:\nDeskripsi: {deskripsi}\nDeadline: {deadline}"
            else:
                return f"Tidak dapat menemukan tugas yang cocok untuk '{tugas_name}' di kelas {kelas_name}."
    else:
        return "Tolong ulangi pertanyaan dan sertakan nama kelas."

# Fungsi untuk mengolah respon dengan kamus sinonim
def respond_to_input(user_input):
    global last_class_requested

    # Mengganti kata-kata dengan sinonimnya
    for key, values in kelas_sinonim.items():
        for value in values:
            user_input = user_input.replace(value, key)

    for pattern, responses in patterns.items():
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            if pattern.startswith(r"(?:apa saja|sebutkan|daftar|apa) (?:tugas|PR)(?: untuk| di)?"):
                last_class_requested = match.group(1).strip().lower()
            elif pattern.startswith(r"(?:info|detail) tugas"):
                if len(match.groups()) == 2:
                    last_class_requested = match.group(2).strip().lower()

            return responses(match.groups())

    return "Maaf, saya tidak mengerti. Bisakah kamu berikan pertanyaan yang lebih detail?"

# Fungsi untuk memulai percakapan dengan chatbot menggunakan GUI
def chatbot_conversation():
    def send_message(event=None):
        user_input = entry.get()
        if user_input.lower() == 'bye':
            window.quit()
        response = respond_to_input(user_input)
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Anda: " + user_input + "\n")
        chat_area.insert(tk.END, "Assitant: " + response + "\n\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)
        
        entry.delete(0, tk.END)

    window = tk.Tk()
    window.title("Eclass Assistant")
    window.iconphoto(True, tk.PhotoImage(file="logo.png"))

    chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(window, width=80)
    entry.pack(padx=10, pady=10, fill=tk.X)
    entry.bind("<Return>", send_message)

    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack(padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    chatbot_conversation()