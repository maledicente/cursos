using System;
using System.Linq;

namespace perceptron
{
    public class Perceptron
    {
        static readonly double[] w = new double[3];
        private readonly int[,] _matrizAprendizado = new int[4, 3];
        private double _net;

        Perceptron()
        {
             //tabela AND
            _matrizAprendizado[0, 0] = 0;
            _matrizAprendizado[0, 1] = 0;
            _matrizAprendizado[0, 2] = 0;

            _matrizAprendizado[1, 0] = 0;
            _matrizAprendizado[1, 1] = 1;
            _matrizAprendizado[1, 2] = 0;

            _matrizAprendizado[2, 0] = 1;
            _matrizAprendizado[2, 1] = 0;
            _matrizAprendizado[2, 2] = 0;

            _matrizAprendizado[3, 0] = 1;
            _matrizAprendizado[3, 1] = 1;
            _matrizAprendizado[3, 2] = 1;

            w[0] = 0;
            w[1] = 0;
            w[2] = 0;
        }

        public static void Main(string[] args)
        {
            //pesos antes do treinamento
            w.ToList().ForEach(x => Console.WriteLine(x + ","));

            Console.WriteLine("\n");

            //efetua-se o treinamento da rede
            new Perceptron().Treinar();

            Console.WriteLine("\n");

            //pesos ajustados após treinamento
            w.ToList().ForEach(x => Console.WriteLine(x + ","));

            //dados de entrada para rede treinada, 0 e 0 resulta em 0 (tabela and) -1 corresponde ao BIAS

            int[] amostra1 = { 0, 1, -1 }; // 0 e 1 -> 0 Classe B
            int[] amostra2 = { 1, 0, -1 }; // 1 e 0 -> 0 Classe B
            int[] amostra3 = { 0, 0, -1 }; // 0 e 0 -> 0 Classe B
            int[] amostra4 = { 1, 1, -1 }; // 1 e 1 -> 1 Classe A


            ClassificarAmostra(amostra1);
            ClassificarAmostra(amostra2);
            ClassificarAmostra(amostra3);
            ClassificarAmostra(amostra4);

            Console.ReadKey();
        }

        public static void ClassificarAmostra(int[] amostra)
        {
            //pesos encontrados após o treinamento
            int[] pesos = { 2, 1, 3 };

            //aplicação da separação dos dados linearmente após aprendizado
            var u = amostra.Select((t, k) => pesos[k] * t).Sum();

            var y = LimiarAtivacao(u);

            Console.WriteLine(y > 0 ? "Amostra da classe A >= 0" : "HelloWorld < 0");
        }

        private static int LimiarAtivacao(double u)
        {
            return (u >= 0) ? 1 : 0;
        }

        int Executar(int x1, int x2)
        {
            _net = (x1 * w[0]) + (x2 * w[1]) + ((-1) * w[2]);

            return (_net >= 0) ? 1 : 0;
        }

        public void Treinar()
        {
            var treinou = true;

            for (var i = 0; i < _matrizAprendizado.GetLength(0); i++)
            {
                var saida = Executar(_matrizAprendizado[i, 0], _matrizAprendizado[i, 1]);

                if (saida != _matrizAprendizado[i, 2])
                {
                    CorrigirPeso(i, saida);

                    treinou = false;
                }
            }

            if (!treinou)
                Treinar();
        }

        void CorrigirPeso(int i, int saida)
        {
            w[0] = w[0] + (1 * (_matrizAprendizado[i, 2] - saida) * _matrizAprendizado[i, 0]);
            w[1] = w[1] + (1 * (_matrizAprendizado[i, 2] - saida) * _matrizAprendizado[i, 1]);
            w[2] = w[2] + (1 * (_matrizAprendizado[i, 2] - saida) * (-1));
        }
    }
}