class Computador:
    def __init__(self, nome):
        self.nome = nome
        self.cpu = CPU()
        self.gpu = GPU()
        self.memoria_ram = MemoriaRAM()
        self.disco_rigido = DiscoRigido()
        self.placa_mae = PlacaMae()
        self.ventoinhas = Ventoinhas()
        self.leds = Leds()

    def ligar(self):
        print(f"{self.nome} foi ligado.")

    def desligar(self):
        print(f"{self.nome} foi desligado.")

    def monitorar(self):
        print("Monitorando componentes:")
        self.cpu.obter_temperatura()
        self.gpu.obter_temperatura()
        self.memoria_ram.verificar_uso()
        self.disco_rigido.verificar_espaco_livre()
        self.placa_mae.verificar_estado()
        self.ventoinhas.verificar_velocidade()
        self.leds.verificar_estado()

class CPU:
    def obter_temperatura(self): 
        temperatura = 60 
        print(f"Temperatura da CPU: {temperatura}°C")

class GPU:
    def obter_temperatura(self):
        temperatura = 70 
        print(f"Temperatura da GPU: {temperatura}°C")

class MemoriaRAM:
    def verificar_uso(self):
        uso = 60
        print(f"Uso da Memória RAM: {uso}%")

class DiscoRigido:
    def verificar_espaco_livre(self):
        espaco_livre = 500
        print(f"Espaço Livre no Disco Rígido: {espaco_livre} GB")

class PlacaMae:
    def verificar_estado(self):
        estado = "funcionando"
        print(f"Estado da Placa-Mãe: {estado}")

class Ventoinhas:
    def verificar_velocidade(self):
        velocidade = 1500
        print(f"Velocidade das ventoinhas: {velocidade} RPM")

class Leds:
    def verificar_estado(self):
        estado = "ligado"
        print(f"Estado dos LEDs: {estado}")
