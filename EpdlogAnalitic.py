from typing import Dict, Union

class EpidemiologiaAnalitica:
    """
    Classe rigorosa para modelagem de dinâmicas populacionais de doenças.
    Implementa validações matemáticas para garantir a integridade de proporções,
    razões e taxas (evitando divisões por zero ou proporções > 1).
    """

    @staticmethod
    def calcular_prevalencia(casos_totais: int, populacao_total: int) -> float:
        """
        Cálculo de Proporção: Prevalência Ponto.
        
        O que é: A proporção da população que apresenta a doença em um instante 't'.
        Não é uma taxa, pois o tempo não compõe o denominador.
        
        Variáveis:
        - casos_totais (Numerador): Indivíduos doentes no momento avaliado (novos + antigos).
        - populacao_total (Denominador): População total (doentes + sadios) no mesmo momento.
        """
        if populacao_total <= 0:
            raise ValueError("A população total deve ser maior que zero.")
        if casos_totais > populacao_total:
            raise ValueError("O número de casos não pode exceder a população total (Proporção > 1).")
        
        return casos_totais / populacao_total

    @staticmethod
    def calcular_incidencia_cumulativa(casos_novos: int, populacao_em_risco: int) -> float:
        """
        Cálculo de Proporção: Incidência Cumulativa (Risco).
        
        O que é: A probabilidade de um indivíduo sadio desenvolver a doença durante
        um período de tempo específico.
        
        Variáveis:
        - casos_novos (Numerador): Casos incidentes (novos) que surgiram no período.
        - populacao_em_risco (Denominador): População no início do período, subtraindo 
          indivíduos que já tinham a doença ou que são imunes.
        """
        if populacao_em_risco <= 0:
            raise ValueError("A população em risco deve ser maior que zero.")
        if casos_novos > populacao_em_risco:
            raise ValueError("Casos novos não podem exceder a população em risco.")
            
        return casos_novos / populacao_em_risco

    @staticmethod
    def calcular_densidade_incidencia(casos_novos: int, pessoas_tempo: float) -> float:
        """
        Cálculo de Taxa Verdadeira: Densidade de Incidência.
        
        O que é: A velocidade com que a doença ocorre na população. Utiliza cálculo
        baseado no tempo exato de contribuição de cada indivíduo.
        
        Variáveis:
        - casos_novos (Numerador): Casos incidentes no período.
        - pessoas_tempo (Denominador): A soma do tempo que cada pessoa permaneceu em risco
          durante o estudo (ex: 10 pessoas acompanhadas por 2 anos = 20 pessoas-ano).
        """
        if pessoas_tempo <= 0:
            raise ValueError("O tempo de risco (pessoas-tempo) deve ser positivo.")
            
        return casos_novos / pessoas_tempo

    @staticmethod
    def calcular_razao(medida_expostos: float, medida_nao_expostos: float) -> float:
        """
        Cálculo de Razão (Ratio): Utilizado para Risco Relativo e Razão de Prevalência.
        
        O que é: Compara a ocorrência da doença entre um grupo submetido a um 
        fator de risco e um grupo controle.
        
        Variáveis:
        - medida_expostos (Numerador): Incidência ou Prevalência no grupo de risco.
        - medida_nao_expostos (Denominador): Incidência ou Prevalência no grupo controle.
        """
        if medida_nao_expostos <= 0:
            raise ValueError("A medida do grupo não exposto deve ser maior que zero para divisão matemática.")
            
        return medida_expostos / medida_nao_expostos


# -----------------------------------------------------------------------------
# FUNÇÕES DE SANITIZAÇÃO DE ENTRADA (I/O)
# -----------------------------------------------------------------------------
def ler_entrada_int(mensagem: str) -> int:
    """Garante que a entrada do usuário seja estritamente um número inteiro."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("[Erro] Entrada inválida. Por favor, digite um número inteiro sem decimais.")


def ler_entrada_float(mensagem: str) -> float:
    """Garante que a entrada do usuário seja um número de ponto flutuante válido."""
    while True:
        try:
            # Substitui vírgula por ponto para evitar erros de cast no padrão brasileiro
            entrada = input(mensagem).replace(',', '.')
            return float(entrada)
        except ValueError:
            print("[Erro] Entrada inválida. Por favor, digite um número decimal válido (ex: 15.5 ou 0.05).")


# -----------------------------------------------------------------------------
# CONSOLE DE EXECUÇÃO INTERATIVA
# -----------------------------------------------------------------------------
def executar_guia_de_estudos():
    """
    Função principal que atua como um console de estudos interativo,
    coletando parâmetros do usuário em tempo real e aplicando teoria epidemiológica.
    """
    calculadora = EpidemiologiaAnalitica()
    
    print("="*60)
    print("MÓDULO DE ESTUDO INTERATIVO: EPIDEMIOLOGIA ANALÍTICA".center(60))
    print("="*60)
    
    # 1. Estudo da Prevalência
    print("\n[1] PREVALÊNCIA (Proporção de estoque)")
    try:
        pop_total = ler_entrada_int("-> Digite a População Total: ")
        casos_existentes = ler_entrada_int("-> Digite os Casos Identificados (novos + antigos): ")
        
        prev = calculadora.calcular_prevalencia(casos_existentes, pop_total)
        print(f"[*] Cálculo: {casos_existentes} / {pop_total}")
        print(f"[*] Resultado: {prev:.4f} ou {prev * 100:.2f}% da população possui a doença.")
    except ValueError as e:
        print(f"[Erro de Validação Matemática] {e}")
    
    # 2. Estudo da Incidência Cumulativa (Risco)
    print("\n[2] INCIDÊNCIA CUMULATIVA (Proporção de risco)")
    try:
        pop_risco = ler_entrada_int("-> Digite a População em Risco (Sadia no Início): ")
        casos_novos = ler_entrada_int("-> Digite os Casos Novos no período: ")
        
        inc_cumulativa = calculadora.calcular_incidencia_cumulativa(casos_novos, pop_risco)
        print(f"[*] Cálculo: {casos_novos} / {pop_risco}")
        print(f"[*] Resultado: {inc_cumulativa:.4f} ou {inc_cumulativa * 100:.2f}% de risco de adoecimento.")
    except ValueError as e:
        print(f"[Erro de Validação Matemática] {e}")
    
    # 3. Estudo da Densidade de Incidência (Taxa verdadeira)
    print("\n[3] DENSIDADE DE INCIDÊNCIA (Taxa de velocidade)")
    
    # Bloco pedagógico explicativo para o aluno
    print("-" * 50)
    print(" CONCEITO: PESSOAS-TEMPO (Denominador Dinâmico)")
    print(" Em vez de contar apenas o número de 'cabeças', somamos")
    print(" o tempo exato que cada pessoa foi acompanhada enquanto")
    print(" estava em risco (saudável).")
    print(" Exemplo Prático:")
    print(" - 100 pessoas acompanhadas por 2 anos = 200 pessoas-ano.")
    print(" - 50 pessoas acompanhadas por 6 meses = 25 pessoas-ano.")
    print("-" * 50)
    
    try:
        casos_novos_densidade = ler_entrada_int("-> Digite os Casos Novos no período: ")
        pessoas_tempo_soma = ler_entrada_float("-> Digite a soma do tempo (Pessoas-Tempo) calculada: ")
        
        densidade = calculadora.calcular_densidade_incidencia(casos_novos_densidade, pessoas_tempo_soma)
        print(f"\n[*] Cálculo executado: {casos_novos_densidade} / {pessoas_tempo_soma}")
        print(f"[*] Resultado: {densidade:.5f}")
        print(f"[*] Interpretação: Ocorrem, em média, {(densidade * 1000):.2f} novos casos a cada 1.000 unidades de tempo (ex: 1.000 pessoas-ano).")
    except ValueError as e:
        print(f"[Erro de Validação Matemática] {e}")
    
    # 4. Estudo de Risco Relativo (Razão)
    print("\n[4] RISCO RELATIVO (Razão de comparação)")
    try:
        incidencia_expostos = ler_entrada_float("-> Digite a Incidência do Grupo Exposto (ex: 0.05 para 5%): ")
        incidencia_controle = ler_entrada_float("-> Digite a Incidência do Grupo Controle (ex: 0.01 para 1%): ")
        
        risco_rel = calculadora.calcular_razao(incidencia_expostos, incidencia_controle)
        print(f"[*] Cálculo: {incidencia_expostos} / {incidencia_controle}")
        print(f"[*] Resultado: RR de {risco_rel:.2f}. O grupo exposto tem {risco_rel} vezes mais risco.")
    except ValueError as e:
        print(f"[Erro de Validação Matemática] {e}")
        
    print("\n" + "="*60)
    print("FIM DO MÓDULO".center(60))
    print("="*60)


if __name__ == "__main__":
    executar_guia_de_estudos()