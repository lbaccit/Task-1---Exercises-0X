import sys
def dilatar_B(N, M):
    return N * N * M * M

def dilatar_C_D(N, M):
    return N * N * M * 2


def ejemplo(N,M):
    operacion_B = dilatar_B(N, M)
    operacion_CD = dilatar_C_D(N, M)

    print("Número de operaciones con B (MxM):", operacion_B)
    print("Número de operaciones con C+D:", operacion_CD)
if __name__ == "__main__":

    N = int(sys.argv[1])
    M = int(sys.argv[2])

    ejemplo(N, M)