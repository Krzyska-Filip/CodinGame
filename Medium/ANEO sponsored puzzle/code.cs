using System;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int speed = int.Parse(Console.ReadLine());
        int lightCount = int.Parse(Console.ReadLine());
        List<int> distance = new List<int>();
        List<int> duration = new List<int>();
        for (int i = 0; i < lightCount; i++)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            distance.Add(int.Parse(inputs[0]));
            duration.Add(int.Parse(inputs[1]));
        }

        for(int i = speed; i >= 0; i--){
            double convSpeed = i / 3.6;
            bool skip = true;

            for(int j = lightCount - 1; j >= 0; j--){
                if( Math.Round((float)distance[j] / convSpeed, 2) % (duration[j] * 2) >= duration[j]) {
                    skip = false;
                    break;
                }
            }
            if(skip){
                Console.WriteLine(i);
                break;
            }
        }
    }
}
