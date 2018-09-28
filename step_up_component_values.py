# Reference:
# http://www.learningaboutelectronics.com/Articles/Switch-mode-power-supply-circuit-with-an-MC34063.php

# Bench test
#
# 3.7 V in
# 5.37 V out
#
# Actual values used
# 180 Ohm -> 220 Ohm
# Rsc -> 0 Ohm (short)
# 100 uF -> 100 uF
# R1 -> 100 Ohms
# R2 -> 330 Ohms
# CO -> 680 uF
# CT -> 150 pF
# L -> 1.5 uH


#
# Inputs
#

V_in = 3.7 # [V]
V_out = 5.0 # [V]

I_out = 2.0

R1 = 1.0 # [ohms]

f = 100.0e3 # Frequncy of circuit [Hz]

V_drop_diode = 0.55 # [V]
V_sat = 0.45 # Saturation voltage of transistor in IC [V]

V_ripple = 0.1

#
# Calculations
#

T_on_over_T_off = (V_out + V_drop_diode - V_in) / (V_in - V_sat)

T_on_plus_T_off = (1 / f) / 1.0e-6 # [us]

T_off = T_on_plus_T_off / (T_on_over_T_off + 1) # [us]
T_on = T_on_plus_T_off - T_off # [us]

C_T = (4.0e-5 * T_on * 1.0e-6) / (1.0e-12) # [pF]

I_peak = 2 * I_out * (T_on_over_T_off + 1) # [A]

R_sc = (0.3 / I_peak) / 1.0e-3 # [mOhms]

L_min = (T_on * (V_in - V_sat) / I_peak) # [uH]

C_o = (9 * (I_out * T_on) / V_ripple) # [uF]

R2 = R1 * ((V_out / 1.25) - 1) # [Ohms]

#
# Print output
#

print("V_in: {} V".format(V_in))
print("V_out: {} V".format(V_out))
print("")
print("R1: {} Ohms".format(R1))
print("R2: {} Ohms".format(R2))
print("R_sc: {} mOhms".format(R_sc))
print("")
print("C_T: {} pF".format(C_T))
print("C_o: {} uF".format(C_o))
print("")
print("L: {} uH".format(L_min))
