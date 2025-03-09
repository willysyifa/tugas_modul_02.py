# ROBOT BATTLE GAME

# Willy Syifa Luthfia
# 123140071

import random
import time    

# Kelas Robot untuk mekanisme pertarungan robot
class Robot:
    def __init__(self, name, hp, attack, defense, accuracy):
        # Inisialisasi atribut robot
        self.name = name
        self.max_hp = hp  
        self.hp = hp
        self.base_attack = attack
        self.attack = attack
        self.base_defense = defense
        self.defense = defense
        self.accuracy = accuracy
        self.stunned = False   # Status efek stun
        self.silenced = False  # Status efek silence
        self.defense_boost = 0  # Peningkatan sementara pada defense

    def attack_enemy(self, enemy):
        # Metode untuk menyerang musuh
        if self.stunned:  
            print(f"{self.name} terkena stun dan tidak bisa menyerang!")
            self.stunned = False  
            return False
        
        if random.random() <= self.accuracy:  
            damage = max(0, self.attack - enemy.defense)  
            enemy.hp = max(0, enemy.hp - damage)  
            print(f"{self.name} menyerang {enemy.name}!")
            print(f"⚔️ {self.name} [Attack: {self.attack}] - {enemy.name} [Defense: {enemy.defense}] ➝ Damage: {damage}")
            return True
        else:
            print(f"{self.name} gagal menyerang.")
            return False

    def defend(self):
        # Metode untuk meningkatkan pertahanan
        self.defense_boost = 5  
        self.defense += self.defense_boost  
        print(f"{self.name} meningkatkan pertahanan sebesar {self.defense_boost}!")
        print(f"🛡️ Defense sekarang: {self.defense}")

    def use_stun(self, enemy):
        # Metode untuk memberikan efek stun pada musuh
        if self.silenced:
            print(f"{self.name} terkena Silence dan tidak bisa menggunakan skill!")
        else:
            print(f"⚡ {self.name} menggunakan Stun pada {enemy.name}!")
            enemy.stunned = True  

    def use_silence(self, enemy):
        # Metode untuk memberikan efek silence pada musuh
        if self.silenced:
            print(f"{self.name} terkena Silence dan tidak bisa menggunakan skill!")
        else:
            print(f"🔇 {self.name} menggunakan Silence pada {enemy.name}!")
            enemy.silenced = True  

    def regen_hp(self):
        # Metode untuk memulihkan HP
        if self.hp < self.max_hp:  
            regen_amount = min(20, self.max_hp - self.hp)  
            self.hp += regen_amount
            print(f"❤️ {self.name} memulihkan {regen_amount} HP!")
        else:
            print(f"{self.name} sudah memiliki HP penuh!")

    def reset_defense(self):
        # Metode untuk mengembalikan pertahanan ke nilai awal
        if self.defense_boost > 0:
            self.defense -= self.defense_boost
            self.defense_boost = 0

    def upgrade_attack(self, round_number):
        # Metode untuk meningkatkan attack setiap 3 ronde
        if round_number % 3 == 0:  
            self.attack += 5
            print(f"🔥 {self.name} mendapatkan peningkatan attack sebesar 5!")

    def is_alive(self):
        # Mengecek apakah robot masih hidup
        return self.hp > 0

# Kelas Game untuk mengatur jalannya permainan
class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1  

    def start(self):
        # Metode untuk memulai permainan
        while self.robot1.is_alive() and self.robot2.is_alive():  
            print(f"\n============================= Round-{self.round} ============================================")
            print(f"{self.robot1.name} [{self.robot1.hp} HP | Attack: {self.robot1.attack} | Defense: {self.robot1.defense}]")
            print(f"{self.robot2.name} [{self.robot2.hp} HP | Attack: {self.robot2.attack} | Defense: {self.robot2.defense}]")
            
            for robot, enemy in [(self.robot1, self.robot2), (self.robot2, self.robot1)]:  
                if not robot.is_alive() or not enemy.is_alive():  
                    break
                
                print("\n1. Attack  2. Defend  3. Stun  4. Silence  5. Give Up  6. Regen HP")

                try:
                    choice = int(input(f"{robot.name}, pilih aksi: "))  
                except ValueError:
                    print("Input tidak valid!")
                    continue
                if choice == 1:
                    robot.attack_enemy(enemy)
                elif choice == 2:
                    robot.defend()
                elif choice == 3:
                    robot.use_stun(enemy)
                elif choice == 4:
                    robot.use_silence(enemy)
                elif choice == 5:
                    print(f"{robot.name} menyerah! {enemy.name} menang!")
                    self.show_result(enemy)
                    return
                elif choice == 6:
                    robot.regen_hp()
                else:
                    print("Pilihan tidak valid!")
                    continue  

                if not enemy.is_alive():  
                    print(f"{enemy.name} kalah! {robot.name} menang!")
                    self.show_result(robot)
                    return
                
                time.sleep(1) 

            self.robot1.reset_defense()
            self.robot2.reset_defense()
            self.robot1.upgrade_attack(self.round)
            self.robot2.upgrade_attack(self.round)
            self.robot1.silenced = False  
            self.robot2.silenced = False  

            print(f"\n------------ Akhir Round-{self.round} ----------------")
            self.round += 1  

    def show_result(self, winner):
        # Metode untuk menampilkan hasil akhir pertandingan
        loser = self.robot1 if winner == self.robot2 else self.robot2
        print("\n============================= Hasil Akhir ===========================================")
        print(f"🏆 Pemenang: {winner.name} dengan {winner.hp} HP!")
        print(f"💀 {loser.name} kalah!")
        print("🎉 Pertarungan selesai! 🎉\n")

# Inisialisasi robot
robot1 = Robot("Titan", 150, 60, 5, 0.75)
robot2 = Robot("Zephyr", 150, 50, 8, 0.75)

# Memulai permainan
game = Game(robot1, robot2)
game.start()

# Program ini adalah permainan **Robot Battle Game**, di mana dua robot bertarung 
# secara bergantian hingga salah satu kalah. Setiap robot memiliki atribut 
# **HP, Attack, Defense, Accuracy**, serta kemampuan khusus seperti **Stun** (mencegah lawan menyerang), 
# **Silence** (mencegah lawan menggunakan skill), **Defend** (meningkatkan pertahanan sementara), 
# dan **Regen HP** (memulihkan HP). Pemain memilih aksi setiap giliran, dan serangan memiliki 
# kemungkinan gagal berdasarkan **accuracy**. Jika serangan berhasil, damage dihitung sebagai 
# **attack - defense lawan**. Setiap 3 ronde, attack robot meningkat **+5**, dan 
# efek **stun, silence, serta peningkatan defense** di-reset di akhir ronde. 
# Permainan berakhir saat salah satu robot **HP-nya mencapai 0** atau menyerah.
