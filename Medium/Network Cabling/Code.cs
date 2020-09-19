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
        int? leftMost = null, rightMost = null;
        int N = int.Parse(Console.ReadLine());
        int[] y = new int[N];

        for (int i = 0; i < N; i++)
        {
            //Read Input
            string[] inputs = Console.ReadLine().Split(' ');
            int x = int.Parse(inputs[0]);
            y[i] = int.Parse(inputs[1]);

            //Find the leftmost house and the rightmost house
            if(leftMost == null || leftMost > x)
               leftMost = x;
            if(rightMost == null || rightMost < x)
               rightMost = x;
        }

        //The distance between the first and last home
        decimal result = Math.Abs((decimal)leftMost - (decimal)rightMost);

        //Sort array to get median
        Array.Sort(y);

        //Find median which will be our new x axis
        int mediana;
        if(y.Length % 2 == 0) {
           mediana = (y[y.Length / 2] + y[y.Length / 2 - 1]) / 2;
        }
        else {
           mediana = y[y.Length / 2];
        }

        //Calculate the distance between each house from the x axis and add it to result
        foreach(int k in y)
        {
            result += Math.Abs((decimal)mediana - (decimal) k);
        }

        Console.WriteLine(result);
    }
}
