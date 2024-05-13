// // namespace MetricsTest;
// // using System;
// // using System.Collections.Generic;
// // using Microsoft.Extensions.DependencyInjection;
// // using System.Diagnostics.Metrics;
// // using ConsoleApp1;
// //
// // public class MetricTests
// // {
// //     [Fact]
// //     public void SaleIncrementsHatsSoldCounter()
// //     {
// //         // Arrange
// //         var services = CreateServiceProvider();
// //         var metrics = services.GetRequiredService<HatCoMetrics>();
// //         var meterFactory = services.GetRequiredService<IMeterFactory>();
// //         var collector = new MetricCollector<int>(meterFactory, "HatCo.Store", "hatco.store.hats_sold");
// //
// //         // Act
// //         metrics.HatsSold(15);
// //
// //         // Assert
// //         var measurements = collector.GetMeasurementSnapshot();
// //         Assert.Equal(1, measurements.Count);
// //         Assert.Equal(15, measurements[0].Value);
// //     }
// //
// //     // Setup a new service provider. This example creates the collection explicitly but you might leverage
// //     // a host or some other application setup code to do this as well.
// //     private static IServiceProvider CreateServiceProvider()
// //     {
// //         var serviceCollection = new ServiceCollection();
// //         serviceCollection.AddMetrics();
// //         serviceCollection.AddSingleton<HatCoMetrics>();
// //         return serviceCollection.BuildServiceProvider();
// //     }
// // }
// namespace MetricsTest;
// using System;
// using System.Collections.Generic;
// using Microsoft.Extensions.DependencyInjection;
// using System.Diagnostics.Metrics;
// using ConsoleApp1;
// class HatCoMetricsWithGlobalMeter
// {
//     static Meter s_meter = new Meter("HatCo.Store");
//     static Counter<int> s_hatsSold = s_meter.CreateCounter<int>("hatco.store.hats_sold");
//
//     public void HatsSold(int quantity)
//     {
//         s_hatsSold.Add(quantity);
//     }
// }
//
// public class MetricTests
// {
//     [Fact]
//     public void SaleIncrementsHatsSoldCounter()
//     {
//         // Arrange
//         var metrics = new HatCoMetricsWithGlobalMeter();
//         // Be careful specifying scope=null. This binds the collector to a global Meter and tests
//         // that use global state should not be configured to run in parallel.
//         var collector = new MetricCollector<int>(null, "HatCo.Store", "hatco.store.hats_sold");
//
//         // Act
//         metrics.HatsSold(15);
//
//         // Assert
//         var measurements = collector.GetMeasurementSnapshot();
//         Assert.Equal(1, measurements.Count);
//         Assert.Equal(15, measurements[0].Value);
//     }
// }

using Xunit;
using System;
using System.Collections.Generic;
using Microsoft.Extensions.DependencyInjection;
using System.Diagnostics.Metrics;
using ConsoleApp1;

namespace MetricsTest
{
    class  CreateServiceProvider
    {
        public void Test()
        {
            
        }
    }
    
    
    public class MetricTests
    {
        [Fact]
        public void Tests()
        {
            // Assert
            Assert.True(true); 
        }
    }
}


