#
def forwardMultiplyGate(a, b):
    return a*b

def forwardAddGate(a, b):
    return a + b

def forwardCircuit(x, y, z):
    q = forwardAddGate(x, y)
    f = forwardMultiplyGate(q, z)
    return f

x = -2
y = 5
z = -4
q = forwardAddGate(x, y)
f = forwardMultiplyGate(q, z)

derivative_f_wrt_z = q
derivative_f_wrt_q = z

derivative_q_wrt_x = 1.0
derivative_q_wrt_y = 1.0

derivative_f_wrt_x = derivative_q_wrt_x * derivative_f_wrt_q
derivative_f_wrt_y = derivative_q_wrt_y * derivative_f_wrt_q

gradient_f_wrt_xyz = [derivative_f_wrt_x, derivative_f_wrt_y, derivative_f_wrt_z]

step_size = 0.01
x = x + step_size * derivative_f_wrt_x
y = y + step_size * derivative_f_wrt_y
z = z + step_size * derivative_f_wrt_z

q = forwardAddGate(x ,y)
f = forwardMultiplyGate(q, z)

print(f)
