using System;

namespace MyApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to MyApp!");

            var calculator = new Calculator();
            Console.WriteLine($"2 + 3 = {calculator.Add(2, 3)}");
            Console.WriteLine($"5 - 3 = {calculator.Subtract(5, 3)}");
        }
    }
}