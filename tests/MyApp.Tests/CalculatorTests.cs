using Xunit;
using MyApp;

namespace MyApp.Tests
{
    public class CalculatorTests
    {
        [Fact]
        public void Add_ReturnsCorrectSum()
        {
            var calculator = new Calculator();
            Assert.Equal(5, calculator.Add(2, 3));
        }

        [Fact]
        public void Subtract_ReturnsCorrectDifference()
        {
            var calculator = new Calculator();
            Assert.Equal(2, calculator.Subtract(5, 3));
        }
    }
}