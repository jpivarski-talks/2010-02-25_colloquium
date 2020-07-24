import ROOT

f1 = ROOT.TF1("f1", "(exp(-x**2)*1)**2", -5, 5)
f2 = ROOT.TF1("f2", "(exp(-x**2)*(2*x))**2", -5, 5)
f3 = ROOT.TF1("f3", "(exp(-x**2)*(4*x**2-2))**2", -5, 5)

f1.Draw()
f2.Draw()
f3.Draw()

