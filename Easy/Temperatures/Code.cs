using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int closestTemp;
        int n = int.Parse(Console.ReadLine()); // the number of temperatures to analyse
        string[] inputs = Console.ReadLine().Split(' ');

        if (n == 0) {
            Console.WriteLine('0');
            return;
        }

        closestTemp = int.Parse(inputs[0]);

        for (int i = 1; i < n; i++) {
            int readInput = int.Parse(inputs[i]);
            if(Math.Abs(readInput) < Math.Abs(closestTemp)) {
                closestTemp = readInput;
            }
            else if((Math.Abs(readInput) == Math.Abs(closestTemp)) && readInput > closestTemp) {
                closestTemp = readInput;
            }
        }
        Console.WriteLine(closestTemp);
    }
}
