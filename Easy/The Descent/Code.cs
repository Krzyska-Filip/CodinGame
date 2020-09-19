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
        while (true) {
            int[] mountainH = new int[8];
            for (int i = 0; i < 8; i++) {
                mountainH[i] = int.Parse(Console.ReadLine()); // represents the height of one mountain.
            }
            int maxValue = mountainH.Max();
            int maxIndex = mountainH.ToList().IndexOf(maxValue);
            Console.WriteLine(maxIndex);
        }
    }
}
