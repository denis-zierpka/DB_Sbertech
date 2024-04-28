using System;
using System.Linq;
using LiteDB;

namespace LiteDBSample
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new LiteDatabase(@"MyData.db"))
            {
                var col = db.GetCollection<Customer>("customers");

                col.Insert(new Customer { Name = "Some Name 1", Age = 30 });
                col.Insert(new Customer { Name = "Some Name 2", Age = 25 });
                col.Insert(new Customer { Name = "Some Name 3", Age = 15 });
                col.Insert(new Customer { Name = "Some Name 4", Age = 10 });

                var results = col.Find(x => x.Age > 20);

                foreach (var customer in results)
                {
                    Console.WriteLine(customer.Name);
                }
            }
        }

        public class Customer
        {
            public int Id { get; set; }
            public string? Name { get; set; }
            public int Age { get; set; }
        }
    }
}
