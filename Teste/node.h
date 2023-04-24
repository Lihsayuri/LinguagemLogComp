#include <iostream>
#include <vector>
#include <llvm-10/llvm/IR/Value.h>

class Structure;
class Program;
class RaceLoop;
class SetUpFunction;
class RadioCheckCondition;
class callSetUp;
class Value;
class Identifier;
class RefVarAtribute;
class CodeGenContext;

class Node {
public:
    virtual ~Node() {}
    virtual llvm::Value* codeGen(CodeGenContext& context) { }
};

class Structure : public Node {
public:
    std::vector<Program*> programs;
    Structure() { }
    virtual llvm::Value* codeGen(CodeGenContext& context) { }

}

class Program : public Structure {
public:
    VarDefinition* varDef;
    RaceLoop* raceLoop;
    SetUpFunction* setUp;
    RadioCheckCondition* radioCheck;
    callSetUp* callSetUp;
    Program(VarDefinition* varDef = nullptr, RaceLoop* raceLoop = nullptr, SetUpFunction* setUp = nullptr, RadioCheckCondition* radioCheck = nullptr, callSetUp* callSetUp = nullptr) : varDef(varDef) , raceLoop(raceLoop), setUp(setUp), radioCheck(radioCheck), callSetUp(callSetUp)  { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class VarDefinition : public Program {
public:
    std::string type;
    Identifier* id;
    Value* value;
    VarDefinition(std::string type, Identifier* id, Value* value) : type(type), id(id), value(value) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class FunctionVarDefinition : public Program {
public:
    std::string type;
    Identifier* id;
    FunctionVarDefinition(std::string type, Identifier* id) : type(type), id(id) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class RaceLoop : public Program {
public:
    Integer* laps;
    Program* program;
    RaceLoop(Integer* laps, Program* program) : laps(laps), program(program) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class SetUpFunction : public Program {
public:
    Identifier* id;
    std::vector<VarDefinition*> varDef;
    Program* program;
    SetUpFunction(Identifier* id, std::vector<VarDefinition*> varDef, Program* program) : id(id), varDef(varDef), program(program) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class RadioCheckCondition : public Program {
public:
    Identifier* id;
    Value* value;
    Program* program_if;
    Program* program_else;
    RadioCheckCondition(Identifier* id, Value* value, Program* program_if, Program* program_else = nullptr) : id(id), value(value), program_if(program_if), program_else(program_else)  { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class callSetUp : public Program {
public:
    Identifier* id;

    callSetUp(Identifier* id) : id(id) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class Value : public Node {
public:
    virtual llvm::Value* codeGen(CodeGenContext& context) { }
}

class Identifier : public Value {
public:
    std::string name;
    Identifier(const std::string& name) : name(name) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class RefVarAtribute : public Value {
public:
    Identifier* id;
    Identifier* atribute;
    RefVarAtribute(Identifier* id, Identifier* atribute) : id(id), atribute(atribute) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}


class Integer : public Value {
public:
    long long value;
    Integer(long long value) : value(value) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class Float : public Value {
public:
    double value;
    Float(double value) : value(value) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class String : public Value {
public:
    std::string value;
    String(const std::string& value) : value(value) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class Boolean : public Value {
public:
    bool value;
    Boolean(bool value) : value(value) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class TupleInt : public Value {
public:
    Integer* first;
    Integer* second;
    TupleInt(Integer* first, Integer* second) : first(first), second(second) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class TupleDRS : public Value {
    public:
    std::string first_sector;
    std::string second_sector;
    std::string third_sector;
    Integer* times;
    TupleDRS(std::string first_sector, std::string second_sector = nullptr, std::string third_sector = nullptr, Integer* times) : first_sector(first_sector), second_sector(second_sector), third_sector(third_sector), times(times) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class Tyre : public Value {
public:
    std::string tyre_type;
    std::string tyre_status;
    Tyre(std::string tyre_type, std::string tyre_status) : tyre_type(tyre_type), tyre_status(tyre_status) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

class TyreSet : public Value {
public:
    Tyre* tyre;
    // defina um ou mais pneus
    TyreSet(Tyre* tyre) : tyre(tyre) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

mySetUp
class Expression : public Value {
public:
    virtual llvm::Value* codeGen(CodeGenContext& context) { }
}

class BinaryOperator : public Expression {
public:
    int op;
    Expression* lhs;
    Expression* rhs;
    BinaryOperator(Expression* lhs, int op, Expression* rhs) : lhs(lhs), rhs(rhs), op(op) { }
    virtual llvm::Value* codeGen(CodeGenContext& context);
}

