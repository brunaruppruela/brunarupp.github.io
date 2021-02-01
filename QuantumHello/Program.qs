
//starts the code
namespace QuantumHello {
    //libraries
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    

    @EntryPoint()
    operation SayHello() : Unit {
        Message("Hello quantum world!");
    }
}
