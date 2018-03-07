from __future__ import print_function
from __future__ import division
import sys
import ROOT as rt
import math
from array import array
from LHEevent import *
from LHEfile import *
import plotTools

if __name__ == '__main__':

    # Name
    fileName = "plots"
    cutName = "cuts"
    cutsOn = True

    # Cuts
    ISO_MAX = 0.1
    PT1_MIN, PT2_MIN, PT3_MIN, PT4_MIN = 25, 25, 10, 5
    PT_MIN = 5
    LEAD_ETA_MAX = 2.1
    ETA_MAX = 2.4
    M12_MIN = 12
    M4L_MIN = 60
    M4L_MAX = 120

    # Histograms
    MLL_BINS, MLL_LOW, MLL_UP = 48, 0, 120
    M4l_r, M4l_s, M4l_w = rt.TH1F("M4l_r", "M4l_r", 80, 50, 130), rt.TH1F("M4l_s", "M4l_s", 80, 50, 130), rt.TH1F("M4l_w", "M4l_w", 80, 50, 130)
    M12_r, M12_s, M12_w = rt.TH1F("M12_r", "M12_r", 100, MLL_LOW, 100), rt.TH1F("M12_s", "M12_s", 100, MLL_LOW, 100), rt.TH1F("M12_w", "M12_w", 100, MLL_LOW, 100)
    M34_r, M34_s, M34_w = rt.TH1F("M34_r", "M34_r", 100, MLL_LOW, 100), rt.TH1F("M34_s", "M34_s", 100, MLL_LOW, 100), rt.TH1F("M34_w", "M34_w", 100, MLL_LOW, 100)
    PT_BINS, PT_LOW, PT_UP = 60, 0, 60
    pT1_r, pT1_s, pT1_w = rt.TH1F("pT1_r", "pT1_r", PT_BINS, PT_LOW, PT_UP), rt.TH1F("pT1_s", "pT1_s", PT_BINS, PT_LOW, PT_UP), rt.TH1F("pT1_w", "pT1_w", PT_BINS, PT_LOW, PT_UP)
    pT2_r, pT2_s, pT2_w = rt.TH1F("pT2_r", "pT2_r", PT_BINS, PT_LOW, PT_UP), rt.TH1F("pT2_s", "pT2_s", PT_BINS, PT_LOW, PT_UP), rt.TH1F("pT2_w", "pT2_w", PT_BINS, PT_LOW, PT_UP)
    pT3_r, pT3_s, pT3_w = rt.TH1F("pT3_r", "pT3_r", PT_BINS, PT_LOW, PT_UP), rt.TH1F("pT3_s", "pT3_s", PT_BINS, PT_LOW, PT_UP), rt.TH1F("pT3_w", "pT3_w", PT_BINS, PT_LOW, PT_UP)
    pT4_r, pT4_s, pT4_w = rt.TH1F("pT4_r", "pT4_r", PT_BINS, PT_LOW, PT_UP), rt.TH1F("pT4_s", "pT4_s", PT_BINS, PT_LOW, PT_UP), rt.TH1F("pT4_w", "pT4_w", PT_BINS, PT_LOW, PT_UP)
    ETA_BINS, ETA_LOW, ETA_UP = 60, -3, 3
    eta1_r, eta1_s, eta1_w = rt.TH1F("eta1_r", "eta1_r", ETA_BINS, ETA_LOW, ETA_UP), rt.TH1F("eta1_s", "eta1_s", ETA_BINS, ETA_LOW, ETA_UP), rt.TH1F("eta1_w", "eta1_w", ETA_BINS, ETA_LOW, ETA_UP)
    eta2_r, eta2_s, eta2_w = rt.TH1F("eta2_r", "eta2_r", ETA_BINS, ETA_LOW, ETA_UP), rt.TH1F("eta2_s", "eta2_s", ETA_BINS, ETA_LOW, ETA_UP), rt.TH1F("eta2_w", "eta2_w", ETA_BINS, ETA_LOW, ETA_UP)
    eta3_r, eta3_s, eta3_w = rt.TH1F("eta3_r", "eta3_r", ETA_BINS, ETA_LOW, ETA_UP), rt.TH1F("eta3_s", "eta3_s", ETA_BINS, ETA_LOW, ETA_UP), rt.TH1F("eta3_w", "eta3_w", ETA_BINS, ETA_LOW, ETA_UP)
    eta4_r, eta4_s, eta4_w = rt.TH1F("eta4_r", "eta4_r", ETA_BINS, ETA_LOW, ETA_UP), rt.TH1F("eta4_s", "eta4_s", ETA_BINS, ETA_LOW, ETA_UP), rt.TH1F("eta4_w", "eta4_w", ETA_BINS, ETA_LOW, ETA_UP)
    PHI_BINS, PHI_LOW, PHI_UP = 64, -3.2, 3.2
    phi1_r, phi1_s, phi1_w = rt.TH1F("phi1_r", "phi1_r", PHI_BINS, PHI_LOW, PHI_UP), rt.TH1F("phi1_s", "phi1_s", PHI_BINS, PHI_LOW, PHI_UP), rt.TH1F("phi1_w", "phi1_w", PHI_BINS, PHI_LOW, PHI_UP)
    phi2_r, phi2_s, phi2_w = rt.TH1F("phi2_r", "phi2_r", PHI_BINS, PHI_LOW, PHI_UP), rt.TH1F("phi2_s", "phi2_s", PHI_BINS, PHI_LOW, PHI_UP), rt.TH1F("phi2_w", "phi2_w", PHI_BINS, PHI_LOW, PHI_UP)
    phi3_r, phi3_s, phi3_w = rt.TH1F("phi3_r", "phi3_r", PHI_BINS, PHI_LOW, PHI_UP), rt.TH1F("phi3_s", "phi3_s", PHI_BINS, PHI_LOW, PHI_UP), rt.TH1F("phi3_w", "phi3_w", PHI_BINS, PHI_LOW, PHI_UP)
    phi4_r, phi4_s, phi4_w = rt.TH1F("phi4_r", "phi4_r", PHI_BINS, PHI_LOW, PHI_UP), rt.TH1F("phi4_s", "phi4_s", PHI_BINS, PHI_LOW, PHI_UP), rt.TH1F("phi4_w", "phi4_w", PHI_BINS, PHI_LOW, PHI_UP)
    DELR_BINS, DELR_LOW, DELR_UP = 60, 0, 6
    DELR_BINS2, DELR_LOW2, DELR_UP2 = 60, 3, 9
    delr_r = rt.TH1F("delr_r", "delr_r", DELR_BINS2, DELR_LOW2, DELR_UP2)
    delr_s = rt.TH1F("delr_s", "delr_s", DELR_BINS2, DELR_LOW2, DELR_UP2)
    delr_w = rt.TH1F("delr_w", "delr_w", DELR_BINS2, DELR_LOW2, DELR_UP2)
    delr12 = rt.TH1F("delr12(Z)", "delr12(Z)Y", DELR_BINS, DELR_LOW, DELR_UP)
    delr34 = rt.TH1F("delr34(U)", "delr34(U)", DELR_BINS, DELR_LOW, DELR_UP)
    delr13 = rt.TH1F("delr13", "delr13", DELR_BINS, DELR_LOW, DELR_UP)
    delr14 = rt.TH1F("delr14", "delr14", DELR_BINS, DELR_LOW, DELR_UP)
    delr23 = rt.TH1F("delr23", "delr23", DELR_BINS, DELR_LOW, DELR_UP)
    delr24 = rt.TH1F("delr24", "delr24", DELR_BINS, DELR_LOW, DELR_UP)
    DPHI_BINS, DPHI_LOW, DPHI_UP = 64, 0, 3.2
    DPHI_BINS2, DPHI_LOW2, DPHI_UP2 = 100, 3.1, 3.2
    dphi_r = rt.TH1F("dphi_r", "dphi_r", DPHI_BINS2, DPHI_LOW2, DPHI_UP2)
    dphi_s = rt.TH1F("dphi_s", "dphi_s", DPHI_BINS2, DPHI_LOW2, DPHI_UP2)
    dphi_w = rt.TH1F("dphi_w", "dphi_w", DPHI_BINS2, DPHI_LOW2, DPHI_UP2)
    dphi12 = rt.TH1F("abs dphi12(Z)", "abs dphi12(Z)", DPHI_BINS, DPHI_LOW, DPHI_UP)
    dphi34 = rt.TH1F("abs dphi34(U)", "abs dphi34(U)", DPHI_BINS, DPHI_LOW, DPHI_UP)
    dphi13 = rt.TH1F("abs dphi13", "abs dphi13", DPHI_BINS, DPHI_LOW, DPHI_UP)
    dphi14 = rt.TH1F("abs dphi14", "abs dphi14", DPHI_BINS, DPHI_LOW, DPHI_UP)
    dphi23 = rt.TH1F("abs dphi23", "abs dphi23", DPHI_BINS, DPHI_LOW, DPHI_UP)
    dphi24 = rt.TH1F("abs dphi24", "abs dphi24", DPHI_BINS, DPHI_LOW, DPHI_UP)

    p1_mother = rt.TH1I("pair 1 mother", "pair 1 mother", 22, 36, 14)
    p2_mother = rt.TH1I("pair 2 mother", "pair 2 mother", 22, 36, 14)

    # Lists to make TGraphs
    M12_arr_r, M34_arr_r, M12_arr_s, M34_arr_s, M12_arr_w, M34_arr_w = array('d'), array('d'), array('d'), array('d'), array('d'), array('d')
    pT1_arr_r, pT2_arr_r, pT3_arr_r, pT4_arr_r = array('d'), array('d'), array('d'), array('d')
    pT1_arr_s, pT2_arr_s, pT3_arr_s, pT4_arr_s = array('d'), array('d'), array('d'), array('d')
    pT1_arr_w, pT2_arr_w, pT3_arr_w, pT4_arr_w = array('d'), array('d'), array('d'), array('d')
    x1_arr_r, x2_arr_r, x3_arr_r, x4_arr_r = array('d'), array('d'), array('d'), array('d')
    y1_arr_r, y2_arr_r, y3_arr_r, y4_arr_r = array('d'), array('d'), array('d'), array('d')
    delr12_arr_r, delr34_arr_r, delr12_arr_s, delr34_arr_s, delr12_arr_w, delr34_arr_w = array('d'), array('d'), array('d'), array('d'), array('d'), array('d')
    dphi12_arr_r, dphi34_arr_r, dphi12_arr_s, dphi34_arr_s, dphi12_arr_w, dphi34_arr_w = array('d'), array('d'), array('d'), array('d'), array('d'), array('d')
    phi12_arr_r, phi34_arr_r, phi12_arr_s, phi34_arr_s, phi12_arr_w, phi34_arr_w = array('d'), array('d'), array('d'), array('d'), array('d'), array('d')
    gam12_arr_r, gam34_arr_r, gam12_arr_s, gam34_arr_s, gam12_arr_w, gam34_arr_w = array('d'), array('d'), array('d'), array('d'), array('d'), array('d')

    # Loop over events
    myLHEfile = LHEfile("../unweighted_events.lhe")
    myLHEfile.setMax(100000)
    eventsReadIn = myLHEfile.readEvents()
    n_acc, n_corrPair, n_corrOrder, n_swapOrder, n_wrong = 0, 0, 0, 0, 0
    for oneEvent in eventsReadIn:
        myLHEevent = LHEevent()
        myLHEevent.fillEvent(oneEvent)
        accepted, correctPair, correctOrder = False, False, False
        particles, mus = [], []
        mu_mother, mu_q = {}, {}
        for i in range(0,len(myLHEevent.Particles)):
            p = myLHEevent.Particles[i]
            particles.append(p)
        for p in particles:
            if abs(p['ID']) == 13:
                mus.append(rt.TLorentzVector(p['Px'], p['Py'], p['Pz'], p['E']))
                mu_mother[mus[-1]] = p['mIdx']
                mu_q[mus[-1]] = p['ID']
        mus.sort(key = rt.TLorentzVector.Pt, reverse = True)
        if mu_q[mus[0]] * mu_q[mus[1]] > 0:
                mus[1], mus[2] = mus[2], mus[1]
        if mu_mother[mus[0]] == mu_mother[mus[1]]:
            correctPair = True

        if cutsOn:
            if (mus[0].Pt() > PT1_MIN and mus[1].Pt() > PT2_MIN
                and mus[2].Pt() > PT3_MIN and mus[3].Pt() > PT4_MIN
                and abs(mus[0].Eta()) < LEAD_ETA_MAX and abs(mus[1].Eta()) < LEAD_ETA_MAX
                and abs(mus[2].Eta()) < ETA_MAX and abs(mus[3].Eta()) < ETA_MAX
                and (mus[0] + mus[1]).M() > M12_MIN
                and M4L_MIN < (mus[0] + mus[1] + mus[2] + mus[3]).M() < M4L_MAX
                ):
                accepted = True
        else:
            if (M4L_MIN < (mus[0] + mus[1] + mus[2] + mus[3]).M() < M4L_MAX
                and abs(mus[0].Eta()) < ETA_MAX and abs(mus[1].Eta()) < ETA_MAX
                and abs(mus[2].Eta()) < ETA_MAX and abs(mus[3].Eta()) < ETA_MAX
                ):
                accepted = True

        if accepted:
            if correctPair:
                p1_mother.Fill(particles[mu_mother[mus[0]]]['ID'])
                p2_mother.Fill(particles[mu_mother[mus[2]]]['ID'])
                if particles[mu_mother[mus[0]]]['ID'] == 23:
                    correctOrder = True

        if accepted:
            n_acc += 1
            if correctPair:
                n_corrPair += 1
                if correctOrder:
                    n_corrOrder += 1
                    M4l_r.Fill((mus[0] + mus[1] + mus[2] + mus[3]).M())
                    M12_r.Fill((mus[0] + mus[1]).M())
                    M34_r.Fill((mus[2] + mus[3]).M())
                    pT1_r.Fill(mus[0].Pt())
                    pT2_r.Fill(mus[1].Pt())
                    pT3_r.Fill(mus[2].Pt())
                    pT4_r.Fill(mus[3].Pt())
                    eta1_r.Fill(mus[0].Eta())
                    eta2_r.Fill(mus[1].Eta())
                    eta3_r.Fill(mus[2].Eta())
                    eta4_r.Fill(mus[3].Eta())
                    phi1_r.Fill(mus[0].Phi())
                    phi2_r.Fill(mus[1].Phi())
                    phi3_r.Fill(mus[2].Phi())
                    phi4_r.Fill(mus[3].Phi())

                    M12_arr_r.append((mus[0] + mus[1]).M())
                    M34_arr_r.append((mus[2] + mus[3]).M())
                    pT1_arr_r.append(mus[0].Pt())
                    pT2_arr_r.append(mus[1].Pt())
                    pT3_arr_r.append(mus[2].Pt())
                    pT4_arr_r.append(mus[3].Pt())
                    delr12_arr_r.append(mus[0].DeltaR(mus[1]))
                    delr34_arr_r.append(mus[2].DeltaR(mus[3]))
                    dphi12_arr_r.append(abs(mus[0].DeltaPhi(mus[1])))
                    dphi34_arr_r.append(abs(mus[2].DeltaPhi(mus[3])))
                    phi12_arr_r.append((mus[0] + mus[1]).Phi())
                    phi34_arr_r.append((mus[2] + mus[3]).Phi())
                    gam12_arr_r.append((mus[0] + mus[1]).Gamma())
                    gam34_arr_r.append((mus[2] + mus[3]).Gamma())

                    delr_r.Fill((mus[0] + mus[1]).DeltaR(mus[2] + mus[3]))
                    dphi_r.Fill((mus[0] + mus[1]).DeltaPhi(mus[2] + mus[3]))
                else:
                    n_swapOrder += 1
                    M4l_s.Fill((mus[0] + mus[1] + mus[2] + mus[3]).M())
                    M12_s.Fill((mus[0] + mus[1]).M())
                    M34_s.Fill((mus[2] + mus[3]).M())
                    pT1_s.Fill(mus[0].Pt())
                    pT2_s.Fill(mus[1].Pt())
                    pT3_s.Fill(mus[2].Pt())
                    pT4_s.Fill(mus[3].Pt())
                    eta1_s.Fill(mus[0].Eta())
                    eta2_s.Fill(mus[1].Eta())
                    eta3_s.Fill(mus[2].Eta())
                    eta4_s.Fill(mus[3].Eta())
                    phi1_s.Fill(mus[0].Phi())
                    phi2_s.Fill(mus[1].Phi())
                    phi3_s.Fill(mus[2].Phi())
                    phi4_s.Fill(mus[3].Phi())

                    M12_arr_s.append((mus[0] + mus[1]).M())
                    M34_arr_s.append((mus[2] + mus[3]).M())
                    pT1_arr_s.append(mus[0].Pt())
                    pT2_arr_s.append(mus[1].Pt())
                    pT3_arr_s.append(mus[2].Pt())
                    pT4_arr_s.append(mus[3].Pt())
                    delr12_arr_s.append(mus[0].DeltaR(mus[1]))
                    delr34_arr_s.append(mus[2].DeltaR(mus[3]))
                    dphi12_arr_s.append(abs(mus[0].DeltaPhi(mus[1])))
                    dphi34_arr_s.append(abs(mus[2].DeltaPhi(mus[3])))
                    phi12_arr_s.append((mus[0] + mus[1]).Phi())
                    phi34_arr_s.append((mus[2] + mus[3]).Phi())
                    gam12_arr_s.append((mus[0] + mus[1]).Gamma())
                    gam34_arr_s.append((mus[2] + mus[3]).Gamma())

                    delr_s.Fill((mus[0] + mus[1]).DeltaR(mus[2] + mus[3]))
                    dphi_s.Fill((mus[0] + mus[1]).DeltaPhi(mus[2] + mus[3]))
            else:
                n_wrong += 1
                M4l_w.Fill((mus[0] + mus[1] + mus[2] + mus[3]).M())
                M12_w.Fill((mus[0] + mus[1]).M())
                M34_w.Fill((mus[2] + mus[3]).M())
                pT1_w.Fill(mus[0].Pt())
                pT2_w.Fill(mus[1].Pt())
                pT3_w.Fill(mus[2].Pt())
                pT4_w.Fill(mus[3].Pt())
                eta1_w.Fill(mus[0].Eta())
                eta2_w.Fill(mus[1].Eta())
                eta3_w.Fill(mus[2].Eta())
                eta4_w.Fill(mus[3].Eta())
                phi1_w.Fill(mus[0].Phi())
                phi2_w.Fill(mus[1].Phi())
                phi3_w.Fill(mus[2].Phi())
                phi4_w.Fill(mus[3].Phi())

                M12_arr_w.append((mus[0] + mus[1]).M())
                M34_arr_w.append((mus[2] + mus[3]).M())
                pT1_arr_w.append(mus[0].Pt())
                pT2_arr_w.append(mus[1].Pt())
                pT3_arr_w.append(mus[2].Pt())
                pT4_arr_w.append(mus[3].Pt())
                delr12_arr_w.append(mus[0].DeltaR(mus[1]))
                delr34_arr_w.append(mus[2].DeltaR(mus[3]))
                dphi12_arr_w.append(abs(mus[0].DeltaPhi(mus[1])))
                dphi34_arr_w.append(abs(mus[2].DeltaPhi(mus[3])))
                phi12_arr_w.append((mus[0] + mus[1]).Phi())
                phi34_arr_w.append((mus[2] + mus[3]).Phi())
                gam12_arr_w.append((mus[0] + mus[1]).Gamma())
                gam34_arr_w.append((mus[2] + mus[3]).Gamma())

                delr_w.Fill((mus[0] + mus[1]).DeltaR(mus[2] + mus[3]))
                dphi_w.Fill((mus[0] + mus[1]).DeltaPhi(mus[2] + mus[3]))

#           eta1_arr.append(Z_mu[0].Eta())
#           eta2_arr.append(Z_mu[1].Eta())
#           eta3_arr.append(U_mu[0].Eta())
#           eta4_arr.append(U_mu[1].Eta())

#           delr12.Fill(Z_mu[0].DeltaR(Z_mu[1]))
#           delr34.Fill(U_mu[0].DeltaR(U_mu[1]))
#           delr13.Fill(Z_mu[0].DeltaR(U_mu[0]))
#           delr14.Fill(Z_mu[0].DeltaR(U_mu[1]))
#           delr23.Fill(Z_mu[1].DeltaR(U_mu[0]))
#           delr24.Fill(Z_mu[1].DeltaR(U_mu[1]))

#           dphi12.Fill(abs(Z_mu[0].DeltaPhi(Z_mu[1])))
#           dphi34.Fill(abs(U_mu[0].DeltaPhi(U_mu[1])))
#           dphi13.Fill(abs(Z_mu[0].DeltaPhi(U_mu[0])))
#           dphi14.Fill(abs(Z_mu[0].DeltaPhi(U_mu[1])))
#           dphi23.Fill(abs(Z_mu[1].DeltaPhi(U_mu[0])))
#           dphi24.Fill(abs(Z_mu[1].DeltaPhi(U_mu[1])))
        del oneEvent, myLHEevent


    # Overlay histograms
    lgnd = rt.TLegend(0.79, 0.79, 0.99, 0.99, "")
    canvas_M4l = rt.TCanvas("M4l", "M4l", 800, 600)
    canvas_M4l.cd()
    M4l_w.Scale(float(1) / M4l_w.Integral())
    M4l_w.SetLineColor(rt.kRed)
    M4l_w.SetLineStyle(rt.kDashed)
    M4l_w.SetLineWidth(2)
    M4l_w.Draw()
    if n_corrOrder > 0:
        M4l_r.Scale(float(1) / M4l_r.Integral())
        M4l_r.SetLineColor(rt.kBlue)
        M4l_r.SetLineWidth(2)
        M4l_r.Draw()
        M4l_w.Draw("SAME")
        lgnd.AddEntry(M4l_r, "Correctly matched", "L")
    if n_swapOrder > 0:
        M4l_s.Scale(float(1) / M4l_s.Integral())
        M4l_s.SetLineColor(rt.kGreen)
        M4l_s.SetLineStyle(rt.kDotted)
        M4l_s.SetLineWidth(2)
        M4l_s.Draw("SAME")
        lgnd.AddEntry(M4l_s, "Pairs swapped", "L")
    lgnd.AddEntry(M4l_w, "Incorrectly matched", "L")
    lgnd.Draw()

    canvas_M12 = rt.TCanvas("M12", "M12", 800, 600)
    canvas_M12.cd()
    M12_w.Scale(float(1) / M12_w.Integral())
    M12_w.SetLineColor(rt.kRed)
    M12_w.SetLineStyle(rt.kDashed)
    M12_w.SetLineWidth(2)
    M12_w.Draw()
    if n_corrOrder > 0:
        M12_r.Scale(float(1) / M12_r.Integral())
        M12_r.SetLineColor(rt.kBlue)
        M12_r.SetLineWidth(2)
        M12_r.Draw()
        M12_w.Draw("SAME")
    if n_swapOrder > 0:
        M12_s.Scale(float(1) / M12_s.Integral())
        M12_s.SetLineColor(rt.kGreen)
        M12_s.SetLineStyle(rt.kDotted)
        M12_s.SetLineWidth(2)
        M12_s.Draw("SAME")
    lgnd.Draw()

    canvas_M34 = rt.TCanvas("M34", "M34", 800, 600)
    canvas_M34.cd()
    M34_w.Scale(float(1) / M34_w.Integral())
    M34_w.SetLineColor(rt.kRed)
    M34_w.SetLineStyle(rt.kDashed)
    M34_w.SetLineWidth(2)
    M34_w.Draw()
    if n_corrOrder > 0:
        M34_r.Scale(float(1) / M34_r.Integral())
        M34_r.SetLineColor(rt.kBlue)
        M34_r.SetLineWidth(2)
        M34_r.Draw()
        M34_w.Draw("SAME")
    if n_swapOrder > 0:
        M34_s.Scale(float(1) / M34_s.Integral())
        M34_s.SetLineColor(rt.kGreen)
        M34_s.SetLineStyle(rt.kDotted)
        M34_s.SetLineWidth(2)
        M34_s.Draw("SAME")
    lgnd.Draw()

    canvas_pT1 = rt.TCanvas("pT1", "pT1", 800, 600)
    canvas_pT1.cd()
    pT1_w.Scale(float(1) / pT1_w.Integral())
    pT1_w.SetLineColor(rt.kRed)
    pT1_w.SetLineStyle(rt.kDashed)
    pT1_w.SetLineWidth(2)
    pT1_w.Draw()
    if n_corrOrder > 0:
        pT1_r.Scale(float(1) / pT1_r.Integral())
        pT1_r.SetLineColor(rt.kBlue)
        pT1_r.SetLineWidth(2)
        pT1_r.Draw()
        pT1_w.Draw("SAME")
    if n_swapOrder > 0:
        pT1_s.Scale(float(1) / pT1_s.Integral())
        pT1_s.SetLineColor(rt.kGreen)
        pT1_s.SetLineStyle(rt.kDotted)
        pT1_s.SetLineWidth(2)
        pT1_s.Draw("SAME")
    lgnd.Draw()

    canvas_pT2 = rt.TCanvas("pT2", "pT2", 800, 600)
    canvas_pT2.cd()
    pT2_w.Scale(float(1) / pT2_w.Integral())
    pT2_w.SetLineColor(rt.kRed)
    pT2_w.SetLineStyle(rt.kDashed)
    pT2_w.SetLineWidth(2)
    pT2_w.Draw()
    if n_corrOrder > 0:
        pT2_r.Scale(float(1) / pT2_r.Integral())
        pT2_r.SetLineColor(rt.kBlue)
        pT2_r.SetLineWidth(2)
        pT2_r.Draw()
        pT2_w.Draw("SAME")
    if n_swapOrder > 0:
        pT2_s.Scale(float(1) / pT2_s.Integral())
        pT2_s.SetLineColor(rt.kGreen)
        pT2_s.SetLineStyle(rt.kDotted)
        pT2_s.SetLineWidth(2)
        pT2_s.Draw("SAME")
    lgnd.Draw()

    canvas_pT3 = rt.TCanvas("pT3", "pT3", 800, 600)
    canvas_pT3.cd()
    pT3_w.Scale(float(1) / pT3_w.Integral())
    pT3_w.SetLineColor(rt.kRed)
    pT3_w.SetLineStyle(rt.kDashed)
    pT3_w.SetLineWidth(2)
    pT3_w.Draw()
    if n_corrOrder > 0:
        pT3_r.Scale(float(1) / pT3_r.Integral())
        pT3_r.SetLineColor(rt.kBlue)
        pT3_r.SetLineWidth(2)
        pT3_r.Draw()
        pT3_w.Draw("SAME")
    if n_swapOrder > 0:
        pT3_s.Scale(float(1) / pT3_s.Integral())
        pT3_s.SetLineColor(rt.kGreen)
        pT3_s.SetLineStyle(rt.kDotted)
        pT3_s.SetLineWidth(2)
        pT3_s.Draw("SAME")
    lgnd.Draw()

    canvas_pT4 = rt.TCanvas("pT4", "pT4", 800, 600)
    canvas_pT4.cd()
    pT4_w.Scale(float(1) / pT4_w.Integral())
    pT4_w.SetLineColor(rt.kRed)
    pT4_w.SetLineStyle(rt.kDashed)
    pT4_w.SetLineWidth(2)
    pT4_w.Draw()
    if n_corrOrder > 0:
        pT4_r.Scale(float(1) / pT4_r.Integral())
        pT4_r.SetLineColor(rt.kBlue)
        pT4_r.SetLineWidth(2)
        pT4_r.Draw()
        pT4_w.Draw("SAME")
    if n_swapOrder > 0:
        pT4_s.Scale(float(1) / pT4_s.Integral())
        pT4_s.SetLineColor(rt.kGreen)
        pT4_s.SetLineStyle(rt.kDotted)
        pT4_s.SetLineWidth(2)
        pT4_s.Draw("SAME")
    lgnd.Draw()

    canvas_eta1 = rt.TCanvas("eta1", "eta1", 800, 600)
    canvas_eta1.cd()
    eta1_w.Scale(float(1) / eta1_w.Integral())
    eta1_w.SetLineColor(rt.kRed)
    eta1_w.SetLineStyle(rt.kDashed)
    eta1_w.SetLineWidth(2)
    eta1_w.Draw()
    if n_corrOrder > 0:
        eta1_r.Scale(float(1) / eta1_r.Integral())
        eta1_r.SetLineColor(rt.kBlue)
        eta1_r.SetLineWidth(2)
        eta1_r.Draw()
        eta1_w.Draw("SAME")
    if n_swapOrder > 0:
        eta1_s.Scale(float(1) / eta1_s.Integral())
        eta1_s.SetLineColor(rt.kGreen)
        eta1_s.SetLineStyle(rt.kDotted)
        eta1_s.SetLineWidth(2)
        eta1_s.Draw("SAME")
    lgnd.Draw()

    canvas_eta2 = rt.TCanvas("eta2", "eta2", 800, 600)
    canvas_eta2.cd()
    eta2_w.Scale(float(1) / eta2_w.Integral())
    eta2_w.SetLineColor(rt.kRed)
    eta2_w.SetLineStyle(rt.kDashed)
    eta2_w.SetLineWidth(2)
    eta2_w.Draw()
    if n_corrOrder > 0:
        eta2_r.Scale(float(1) / eta2_r.Integral())
        eta2_r.SetLineColor(rt.kBlue)
        eta2_r.SetLineWidth(2)
        eta2_r.Draw()
        eta2_w.Draw("SAME")
    if n_swapOrder > 0:
        eta2_s.Scale(float(1) / eta2_s.Integral())
        eta2_s.SetLineColor(rt.kGreen)
        eta2_s.SetLineStyle(rt.kDotted)
        eta2_s.SetLineWidth(2)
        eta2_s.Draw("SAME")
    lgnd.Draw()

    canvas_eta3 = rt.TCanvas("eta3", "eta3", 800, 600)
    canvas_eta3.cd()
    eta3_w.Scale(float(1) / eta3_w.Integral())
    eta3_w.SetLineColor(rt.kRed)
    eta3_w.SetLineStyle(rt.kDashed)
    eta3_w.SetLineWidth(2)
    eta3_w.Draw()
    if n_corrOrder > 0:
        eta3_r.Scale(float(1) / eta3_r.Integral())
        eta3_r.SetLineColor(rt.kBlue)
        eta3_r.SetLineWidth(2)
        eta3_r.Draw()
        eta3_w.Draw("SAME")
    if n_swapOrder > 0:
        eta3_s.Scale(float(1) / eta3_s.Integral())
        eta3_s.SetLineColor(rt.kGreen)
        eta3_s.SetLineStyle(rt.kDotted)
        eta3_s.SetLineWidth(2)
        eta3_s.Draw("SAME")
    lgnd.Draw()

    canvas_eta4 = rt.TCanvas("eta4", "eta4", 800, 600)
    canvas_eta4.cd()
    eta4_w.Scale(float(1) / eta4_w.Integral())
    eta4_w.SetLineColor(rt.kRed)
    eta4_w.SetLineStyle(rt.kDashed)
    eta4_w.SetLineWidth(2)
    eta4_w.Draw()
    if n_corrOrder > 0:
        eta4_r.Scale(float(1) / eta4_r.Integral())
        eta4_r.SetLineColor(rt.kBlue)
        eta4_r.SetLineWidth(2)
        eta4_r.Draw()
        eta4_w.Draw("SAME")
    if n_swapOrder > 0:
        eta4_s.Scale(float(1) / eta4_s.Integral())
        eta4_s.SetLineColor(rt.kGreen)
        eta4_s.SetLineStyle(rt.kDotted)
        eta4_s.SetLineWidth(2)
        eta4_s.Draw("SAME")
    lgnd.Draw()

    canvas_phi1 = rt.TCanvas("phi1", "phi1", 800, 600)
    canvas_phi1.cd()
    phi1_w.Scale(float(1) / phi1_w.Integral())
    phi1_w.SetLineColor(rt.kRed)
    phi1_w.SetLineStyle(rt.kDashed)
    phi1_w.SetLineWidth(2)
    phi1_w.Draw()
    if n_corrOrder > 0:
        phi1_r.Scale(float(1) / phi1_r.Integral())
        phi1_r.SetLineColor(rt.kBlue)
        phi1_r.SetLineWidth(2)
        phi1_r.Draw()
        phi1_w.Draw("SAME")
    if n_swapOrder > 0:
        phi1_s.Scale(float(1) / phi1_s.Integral())
        phi1_s.SetLineColor(rt.kGreen)
        phi1_s.SetLineStyle(rt.kDotted)
        phi1_s.SetLineWidth(2)
        phi1_s.Draw("SAME")
    lgnd.Draw()

    canvas_phi2 = rt.TCanvas("phi2", "phi2", 800, 600)
    canvas_phi2.cd()
    phi2_w.Scale(float(1) / phi2_w.Integral())
    phi2_w.SetLineColor(rt.kRed)
    phi2_w.SetLineStyle(rt.kDashed)
    phi2_w.SetLineWidth(2)
    phi2_w.Draw()
    if n_corrOrder > 0:
        phi2_r.Scale(float(1) / phi2_r.Integral())
        phi2_r.SetLineColor(rt.kBlue)
        phi2_r.SetLineWidth(2)
        phi2_r.Draw()
        phi2_w.Draw("SAME")
    if n_swapOrder > 0:
        phi2_s.Scale(float(1) / phi2_s.Integral())
        phi2_s.SetLineColor(rt.kGreen)
        phi2_s.SetLineStyle(rt.kDotted)
        phi2_s.SetLineWidth(2)
        phi2_s.Draw("SAME")
    lgnd.Draw()

    canvas_phi3 = rt.TCanvas("phi3", "phi3", 800, 600)
    canvas_phi3.cd()
    phi3_w.Scale(float(1) / phi3_w.Integral())
    phi3_w.SetLineColor(rt.kRed)
    phi3_w.SetLineStyle(rt.kDashed)
    phi3_w.SetLineWidth(2)
    phi3_w.Draw()
    if n_corrOrder > 0:
        phi3_r.Scale(float(1) / phi3_r.Integral())
        phi3_r.SetLineColor(rt.kBlue)
        phi3_r.SetLineWidth(2)
        phi3_r.Draw()
        phi3_w.Draw("SAME")
    if n_swapOrder > 0:
        phi3_s.Scale(float(1) / phi3_s.Integral())
        phi3_s.SetLineColor(rt.kGreen)
        phi3_s.SetLineStyle(rt.kDotted)
        phi3_s.SetLineWidth(2)
        phi3_s.Draw("SAME")
    lgnd.Draw()

    canvas_phi4 = rt.TCanvas("phi4", "phi4", 800, 600)
    canvas_phi4.cd()
    phi4_w.Scale(float(1) / phi4_w.Integral())
    phi4_w.SetLineColor(rt.kRed)
    phi4_w.SetLineStyle(rt.kDashed)
    phi4_w.SetLineWidth(2)
    phi4_w.Draw()
    if n_corrOrder > 0:
        phi4_r.Scale(float(1) / phi4_r.Integral())
        phi4_r.SetLineColor(rt.kBlue)
        phi4_r.SetLineWidth(2)
        phi4_r.Draw()
        phi4_w.Draw("SAME")
    if n_swapOrder > 0:
        phi4_s.Scale(float(1) / phi4_s.Integral())
        phi4_s.SetLineColor(rt.kGreen)
        phi4_s.SetLineStyle(rt.kDotted)
        phi4_s.SetLineWidth(2)
        phi4_s.Draw("SAME")
    lgnd.Draw()

    # Create dummy graph for line
    line_arr = array('d')
    line_arr.append(0)
    line_arr.append(100)
    graph_line = rt.TGraph(2, line_arr, line_arr)
    graph_line.SetLineColor(rt.kBlack)
    graph_line.SetLineWidth(2)

    # Create scatter plots
    mSize = 0.5
    lgnd2 = rt.TLegend(0.79, 0.79, 0.99, 0.99)
    canvas_Mll = rt.TCanvas("Mll", "Mll", 800, 600)
    canvas_Mll.cd()
    graph_Mll_w = rt.TGraph(n_wrong, M12_arr_w, M34_arr_w)
    graph_Mll_w.GetXaxis().SetTitle('M_{12}(Z)')
    graph_Mll_w.GetYaxis().SetTitle('M_{34}(U)')
    graph_Mll_w.SetMarkerStyle(rt.kFullCircle)
    graph_Mll_w.SetMarkerSize(mSize)
    graph_Mll_w.SetMarkerColor(rt.kRed)
    graph_Mll_w.Draw("AP")
    if n_corrOrder > 0:
        graph_Mll_r = rt.TGraph(n_corrOrder, M12_arr_r, M34_arr_r)
        graph_Mll_r.SetMarkerStyle(rt.kFullCircle)
        graph_Mll_r.SetMarkerSize(mSize)
        graph_Mll_r.SetMarkerColor(rt.kBlue)
        graph_Mll_r.Draw("P")
        lgnd2.AddEntry(graph_Mll_r, "Correctly matched", "P")
        graph_Mll_w.Draw("P")
    lgnd2.AddEntry(graph_Mll_w, "Incorrectly matched", "P")
    if n_swapOrder > 0:
        graph_Mll_s = rt.TGraph(n_swapOrder, M12_arr_s, M34_arr_s)
        graph_Mll_s.SetMarkerStyle(rt.kFullCircle)
        graph_Mll_s.SetMarkerSize(mSize)
        graph_Mll_s.SetMarkerColor(rt.kGreen)
        graph_Mll_s.Draw("P")
        lgnd2.AddEntry(graph_Mll_s, "Pairs swapped", "P")
    graph_line.Draw("L")
    lgnd2.Draw()

    canvas_pT23 = rt.TCanvas("pT23", "pT23", 800, 600)
    canvas_pT23.cd()
    graph_pT23_w = rt.TGraph(n_wrong, pT2_arr_w, pT3_arr_w)
    graph_pT23_w.SetMarkerStyle(rt.kFullCircle)
    graph_pT23_w.SetMarkerSize(mSize)
    graph_pT23_w.SetMarkerColor(rt.kRed)
    graph_pT23_w.Draw("AP")
    if n_corrOrder > 0:
        graph_pT23_r = rt.TGraph(n_corrOrder, pT2_arr_r, pT3_arr_r)
        graph_pT23_r.GetXaxis().SetTitle('p_{T2}')
        graph_pT23_r.GetYaxis().SetTitle('p_{T3}')
        graph_pT23_r.SetMarkerStyle(rt.kFullCircle)
        graph_pT23_r.SetMarkerSize(mSize)
        graph_pT23_r.SetMarkerColor(rt.kBlue)
        graph_pT23_r.Draw("AP")
        graph_pT23_w.Draw("P")
    if n_swapOrder > 0:
        graph_pT23_s = rt.TGraph(n_swapOrder, pT2_arr_s, pT3_arr_s)
        graph_pT23_s.SetMarkerStyle(rt.kFullCircle)
        graph_pT23_s.SetMarkerSize(mSize)
        graph_pT23_s.SetMarkerColor(rt.kGreen)
        graph_pT23_s.Draw("P")
    graph_line.Draw("L")
    lgnd2.Draw()

    canvas_delr = rt.TCanvas("DeltaR", "DeltaR", 800, 600)
    canvas_delr.cd()
    graph_delr_w = rt.TGraph(n_wrong, delr12_arr_w, delr34_arr_w)
    graph_delr_w.GetXaxis().SetTitle('#DeltaR_{12}(Z)')
    graph_delr_w.GetYaxis().SetTitle('#DeltaR_{34}(U)')
    graph_delr_w.SetMarkerStyle(rt.kFullCircle)
    graph_delr_w.SetMarkerSize(mSize)
    graph_delr_w.SetMarkerColor(rt.kRed)
    graph_delr_w.Draw("AP")
    if n_corrOrder > 0:
        graph_delr_r = rt.TGraph(n_corrOrder, delr12_arr_r, delr34_arr_r)
        graph_delr_r.SetMarkerStyle(rt.kFullCircle)
        graph_delr_r.SetMarkerSize(mSize)
        graph_delr_r.SetMarkerColor(rt.kBlue)
        graph_delr_r.Draw("P")
        graph_delr_w.Draw("P")
    if n_swapOrder > 0:
        graph_delr_s = rt.TGraph(n_swapOrder, delr12_arr_s, delr34_arr_s)
        graph_delr_s.SetMarkerStyle(rt.kFullCircle)
        graph_delr_s.SetMarkerSize(mSize)
        graph_delr_s.SetMarkerColor(rt.kGreen)
        graph_delr_s.Draw("P")
    graph_line.Draw("L")
    lgnd2.Draw()

    canvas_dphi = rt.TCanvas("DeltaPhi", "DeltaPhi", 800, 600)
    canvas_dphi.cd()
    graph_dphi_w = rt.TGraph(n_wrong, dphi12_arr_w, dphi34_arr_w)
    graph_dphi_w.GetXaxis().SetTitle('|#Delta#phi_{12}|(Z)')
    graph_dphi_w.GetYaxis().SetTitle('|#Delta#phi_{34}|(U)')
    graph_dphi_w.SetMarkerStyle(rt.kFullCircle)
    graph_dphi_w.SetMarkerSize(mSize)
    graph_dphi_w.SetMarkerColor(rt.kRed)
    graph_dphi_w.Draw("AP")
    if n_corrOrder > 0:
        graph_dphi_r = rt.TGraph(n_corrOrder, dphi12_arr_r, dphi34_arr_r)
        graph_dphi_r.SetMarkerStyle(rt.kFullCircle)
        graph_dphi_r.SetMarkerSize(mSize)
        graph_dphi_r.SetMarkerColor(rt.kBlue)
        graph_dphi_r.Draw("P")
        graph_dphi_w.Draw("P")
    if n_swapOrder > 0:
        graph_dphi_s = rt.TGraph(n_swapOrder, dphi12_arr_s, dphi34_arr_s)
        graph_dphi_s.SetMarkerStyle(rt.kFullCircle)
        graph_dphi_s.SetMarkerSize(mSize)
        graph_dphi_s.SetMarkerColor(rt.kGreen)
        graph_dphi_s.Draw("P")
    graph_line.Draw("L")
    lgnd2.Draw()

    canvas_gamma = rt.TCanvas("Gamma", "Gamma", 800, 600)
    canvas_gamma.cd()
    graph_gamma_w = rt.TGraph(n_wrong, gam12_arr_w, gam34_arr_w)
    graph_gamma_w.GetXaxis().SetTitle('#gamma_{12}(Z)')
    graph_gamma_w.GetYaxis().SetTitle('#gamma_{34}(U)')
    graph_gamma_w.SetMarkerStyle(rt.kFullCircle)
    graph_gamma_w.SetMarkerSize(mSize)
    graph_gamma_w.SetMarkerColor(rt.kRed)
    graph_gamma_w.Draw("AP")
    if n_corrOrder > 0:
        graph_gamma_r = rt.TGraph(n_corrOrder, gam12_arr_r, gam34_arr_r)
        graph_gamma_r.SetMarkerStyle(rt.kFullCircle)
        graph_gamma_r.SetMarkerSize(mSize)
        graph_gamma_r.SetMarkerColor(rt.kBlue)
        graph_gamma_r.Draw("P")
        graph_gamma_w.Draw("P")
    if n_swapOrder > 0:
        graph_gamma_s = rt.TGraph(n_swapOrder, gam12_arr_s, gam34_arr_s)
        graph_gamma_s.SetMarkerStyle(rt.kFullCircle)
        graph_gamma_s.SetMarkerSize(mSize)
        graph_gamma_s.SetMarkerColor(rt.kGreen)
        graph_gamma_s.Draw("P")
    graph_line.Draw("L")
    lgnd2.Draw()

#   canvas_phi = rt.TCanvas("Phi", "Phi", 800, 600)
#   canvas_phi.cd()
#   graph_phi_w = rt.TGraph(n_wrong, phi12_arr_w, phi34_arr_w)
#   graph_phi_w.GetXaxis().SetTitle('#phi_{12}(Z)')
#   graph_phi_w.GetYaxis().SetTitle('#phi_{34}(U)')
#   graph_phi_w.SetMarkerStyle(rt.kFullCircle)
#   graph_phi_w.SetMarkerSize(mSize)
#   graph_phi_w.SetMarkerColor(rt.kRed)
#   graph_phi_w.Draw("AP")
#   graph_phi_r = rt.TGraph(n_corrOrder, phi12_arr_r, phi34_arr_r)
#   graph_phi_r.SetMarkerStyle(rt.kFullCircle)
#   graph_phi_r.SetMarkerSize(mSize)
#   graph_phi_r.SetMarkerColor(rt.kBlue)
#   graph_phi_r.Draw("P")
#   if n_swapOrder > 0:
#       graph_phi_s = rt.TGraph(n_swapOrder, phi12_arr_s, phi34_arr_s)
#       graph_phi_s.SetMarkerStyle(rt.kFullCircle)
#       graph_phi_s.SetMarkerSize(mSize)
#       graph_phi_s.SetMarkerColor(rt.kGreen)
#       graph_phi_s.Draw("P")
#   lgnd2.Draw()

#   graph_ZpT = rt.TGraph(n_acc, pT1_arr, pT2_arr)
#   graph_ZpT.GetXaxis().SetTitle('p_{T1}(Z)')
#   graph_ZpT.GetYaxis().SetTitle('p_{T2}(Z)')
#   graph_ZpT.SetMarkerStyle(rt.kFullCircle)
#   graph_ZpT.SetMarkerSize(0.5)
#   canvas_ZpT = rt.TCanvas("Z muon pT", "Z muon pT", 800, 600)
#   canvas_ZpT.cd()
#   graph_ZpT.Draw("AP")
#   graph_line.Draw("L")

#   graph_UpT = rt.TGraph(n_acc, pT3_arr, pT4_arr)
#   graph_UpT.GetXaxis().SetTitle('p_{T3}(U)')
#   graph_UpT.GetYaxis().SetTitle('p_{T4}(U)')
#   graph_UpT.SetMarkerStyle(rt.kFullCircle)
#   graph_UpT.SetMarkerSize(0.5)
#   canvas_UpT = rt.TCanvas("U muon pT", "U muon pT", 800, 600)
#   canvas_UpT.cd()
#   graph_UpT.Draw("AP")
#   graph_line.Draw("L")

#   graph_pT13 = rt.TGraph(n_acc, pT1_arr, pT3_arr)
#   graph_pT13.GetXaxis().SetTitle('p_{T1}(Z)')
#   graph_pT13.GetYaxis().SetTitle('p_{T3}(U)')
#   graph_pT13.SetMarkerStyle(rt.kFullCircle)
#   graph_pT13.SetMarkerSize(0.5)
#   canvas_pT13 = rt.TCanvas("High U vs High Z pT", "High U vs High Z pT", 800, 600)
#   canvas_pT13.cd()
#   graph_pT13.Draw("AP")
#   graph_line.Draw("L")

#   graph_pT14 = rt.TGraph(n_acc, pT1_arr, pT4_arr)
#   graph_pT14.GetXaxis().SetTitle('p_{T1}(Z)')
#   graph_pT14.GetYaxis().SetTitle('p_{T4}(U)')
#   graph_pT14.SetMarkerStyle(rt.kFullCircle)
#   graph_pT14.SetMarkerSize(0.5)
#   canvas_pT14 = rt.TCanvas("Low U vs High Z pT", "Low U vs High Z pT", 800, 600)
#   canvas_pT14.cd()
#   graph_pT14.Draw("AP")
#   graph_line.Draw("L")

#   graph_pT23 = rt.TGraph(n_acc, pT2_arr, pT3_arr)
#   graph_pT23.GetXaxis().SetTitle('p_{T2}(Z)')
#   graph_pT23.GetYaxis().SetTitle('p_{T3}(U)')
#   graph_pT23.SetMarkerStyle(rt.kFullCircle)
#   graph_pT23.SetMarkerSize(0.5)
#   canvas_pT23 = rt.TCanvas("High U vs Low Z pT", "High U vs Low Z pT", 800, 600)
#   canvas_pT23.cd()
#   graph_pT23.Draw("AP")
#   graph_line.Draw("L")

#   graph_pT24 = rt.TGraph(n_acc, pT2_arr, pT4_arr)
#   graph_pT24.GetXaxis().SetTitle('p_{T2}(Z)')
#   graph_pT24.GetYaxis().SetTitle('p_{T4}(U)')
#   graph_pT24.SetMarkerStyle(rt.kFullCircle)
#   graph_pT24.SetMarkerSize(0.5)
#   canvas_pT24 = rt.TCanvas("Low U vs Low Z pT", "Low U vs Low Z pT", 800, 600)
#   canvas_pT24.cd()
#   graph_pT24.Draw("AP")
#   graph_line.Draw("L")

#   graph_Zeta = rt.TGraph(n_acc, eta1_arr, eta2_arr)
#   graph_Zeta.GetXaxis().SetTitle('#eta_{1}(Z)')
#   graph_Zeta.GetYaxis().SetTitle('#eta_{2}(Z)')
#   graph_Zeta.SetMarkerStyle(rt.kFullCircle)
#   graph_Zeta.SetMarkerSize(0.5)
#   canvas_Zeta = rt.TCanvas("Z muon eta", "Z muon eta", 800, 600)
#   canvas_Zeta.cd()
#   graph_Zeta.Draw("AP")

#   graph_Ueta = rt.TGraph(n_acc, eta3_arr, eta4_arr)
#   graph_Ueta.GetXaxis().SetTitle('#eta_{3}(U)')
#   graph_Ueta.GetYaxis().SetTitle('#eta_{4}(U)')
#   graph_Ueta.SetMarkerStyle(rt.kFullCircle)
#   graph_Ueta.SetMarkerSize(0.5)
#   canvas_Ueta = rt.TCanvas("U muon eta", "U muon eta", 800, 600)
#   canvas_Ueta.cd()
#   graph_Ueta.Draw("AP")

    # Write hists and graphs
    if cutsOn:
        fileName = fileName + "_" + cutName
    fileName = fileName + ".root"
    outFile = rt.TFile(fileName, "RECREATE")
    outFile.mkdir("Histograms")
    outFile.cd("Histograms")
    p1_mother.Write()
    p2_mother.Write()

    delr_r.Write()
    delr_s.Write()
    delr_w.Write()
    dphi_r.Write()
    dphi_s.Write()
    dphi_w.Write()
    M4l_r.Write()
    M12_r.Write()
    M34_r.Write()
    pT1_r.Write()
    pT2_r.Write()
    pT3_r.Write()
    pT4_r.Write()
    eta1_r.Write()
    eta2_r.Write()
    eta3_r.Write()
    eta4_r.Write()
    phi1_r.Write()
    phi2_r.Write()
    phi3_r.Write()
    phi4_r.Write()
    M4l_s.Write()
    M12_s.Write()
    M34_s.Write()
    pT1_s.Write()
    pT2_s.Write()
    pT3_s.Write()
    pT4_s.Write()
    eta1_s.Write()
    eta2_s.Write()
    eta3_s.Write()
    eta4_s.Write()
    phi1_s.Write()
    phi2_s.Write()
    phi3_s.Write()
    phi4_s.Write()
    M4l_w.Write()
    M12_w.Write()
    M34_w.Write()
    pT1_w.Write()
    pT2_w.Write()
    pT3_w.Write()
    pT4_w.Write()
    eta1_w.Write()
    eta2_w.Write()
    eta3_w.Write()
    eta4_w.Write()
    phi1_w.Write()
    phi2_w.Write()
    phi3_w.Write()
    phi4_w.Write()
    outFile.cd()
    outFile.mkdir("Overlays")
    outFile.cd("Overlays")
    canvas_M4l.Write()
    canvas_M12.Write()
    canvas_M34.Write()
    canvas_pT1.Write()
    canvas_pT2.Write()
    canvas_pT3.Write()
    canvas_pT4.Write()
    canvas_eta1.Write()
    canvas_eta2.Write()
    canvas_eta3.Write()
    canvas_eta4.Write()
    canvas_phi1.Write()
    canvas_phi2.Write()
    canvas_phi3.Write()
    canvas_phi4.Write()

    outFile.cd()
    outFile.mkdir("Scatterplots")
    outFile.cd("Scatterplots")
    canvas_Mll.Write()
    canvas_pT23.Write()
    canvas_delr.Write()
    canvas_dphi.Write()
    canvas_gamma.Write()
#   canvas_phi.Write()

#   canvas_ZpT.Write()
#   canvas_UpT.Write()
#   canvas_pT13.Write()
#   canvas_pT14.Write()
#   canvas_pT23.Write()
#   canvas_pT24.Write()
#   canvas_Zeta.Write()
#   canvas_Ueta.Write()
#   outFile.cd()
#   outFile.mkdir("deltaR")
#   outFile.cd("deltaR")
#   delr12.Write()
#   delr34.Write()
#   delr13.Write()
#   delr14.Write()
#   delr23.Write()
#   delr24.Write()
#   outFile.cd()
#   outFile.mkdir("deltaPhi")
#   outFile.cd("deltaPhi")
#   dphi12.Write()
#   dphi34.Write()
#   dphi13.Write()
#   dphi14.Write()
#   dphi23.Write()
#   dphi24.Write()
    outFile.cd()
    outFile.Close()

    # Print info
    print("Accepted", n_acc, "events (of 100000)")
    print("With correct matching:\t", n_corrOrder, "\t", float(n_corrOrder) / float(n_acc))
    print("With pairs swapped:\t", n_swapOrder, "\t", float(n_swapOrder) / float(n_acc))
    print("With incorrect matching:", n_wrong, "\t", float(n_wrong) / float(n_acc))
    print("\nCreated file", fileName)


#   del M4l, M12, M34, pT1, pT2, pT3, pT4, eta1, eta2, eta3, eta4, phi1, phi2, phi3, phi4
#   del delr12, delr34, delr13, delr14, delr23, delr24
#   del graph_Mll, graph_ZpT, graph_UpT, graph_pT13, graph_pT14, graph_pT23, graph_pT24, graph_Zeta, graph_Ueta, graph_delr, graph_dphi
#   del canvas_Mll, canvas_ZpT, canvas_UpT, canvas_pT13, canvas_pT14, canvas_pT23, canvas_pT24, canvas_Zeta, canvas_Ueta, canvas_delr, canvas_dphi