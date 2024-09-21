from ortools.sat.python import cp_model

if  __name__ == '__main__':
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    freqs = {0: 'f1', 1: 'f2', 2: 'f3'}
    A1 = model.NewIntVar(0, 2, 'Antenna 1')
    A2 = model.NewIntVar(0, 2, 'Antenna 2')
    A3 = model.NewIntVar(0, 2, 'Antenna 3')
    A4 = model.NewIntVar(0, 2, 'Antenna 4')
    A5 = model.NewIntVar(0, 2, 'Antenna 5')
    A6 = model.NewIntVar(0, 2, 'Antenna 6')
    A7 = model.NewIntVar(0, 2, 'Antenna 7')
    A8 = model.NewIntVar(0, 2, 'Antenna 8')
    A9 = model.NewIntVar(0, 2, 'Antenna 9')

    model.Add(A1 != A2)
    model.Add(A1 != A3)
    model.Add(A1 != A4)
    model.Add(A2 != A3)
    model.Add(A2 != A5)
    model.Add(A2 != A6)
    model.Add(A3 != A6)
    model.Add(A3 != A9)
    model.Add(A4 != A5)
    model.Add(A6 != A7)
    model.Add(A6 != A8)
    model.Add(A7 != A8)
    model.Add(A8 != A9)

    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("A1: %s" % freqs[solver.Value(A1)])
        print("A2: %s" % freqs[solver.Value(A2)])
        print("A3: %s" % freqs[solver.Value(A3)])
        print("A4: %s" % freqs[solver.Value(A4)])
        print("A5: %s" % freqs[solver.Value(A5)])
        print("A6: %s" % freqs[solver.Value(A6)])
        print("A7: %s" % freqs[solver.Value(A7)])
        print("A8: %s" % freqs[solver.Value(A8)])
        print("A9: %s" % freqs[solver.Value(A9)])







