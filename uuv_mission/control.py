class PDController:
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def control_action(self, error: float) -> float:
        derivative = error - self.previous_error
        action = self.kp * error + self.kd * derivative
        self.previous_error = error
        return action