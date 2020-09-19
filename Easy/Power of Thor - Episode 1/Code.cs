using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Player
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]);
        int lightY = int.Parse(inputs[1]);
        int initialTx = int.Parse(inputs[2]);
        int initialTy = int.Parse(inputs[3]);

        while (true) {
            int remainingTurns = int.Parse(Console.ReadLine());
            string move = "";
            if(initialTy > lightY) {
                move += 'N';
                initialTy--;
            }
            else if (initialTy < lightY) {
                move += 'S';
                initialTy++;
            }

            if(initialTx > lightX) {
                move += 'W';
                initialTx--;
            }
            else if (initialTx < lightX) {
                move += 'E';
                initialTx++;
            }
            Console.WriteLine(move);
        }
    }
}
