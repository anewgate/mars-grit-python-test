import time

from pca9685 import PCA9685
import pca9685



def map_angle_to_pulse(angle):
    """
    각도(0~180)를 펄스 폭(500us ~ 2500us)으로 매핑하는 함수
    일반적인 서보모터 기준: 0도=500us, 180도=2500us
    """
    min_pulse = 500
    max_pulse = 2500
    pulse = min_pulse + (angle * (max_pulse - min_pulse) / 180)
    return pulse


if __name__ == '__main__':
    # 1. 객체 초기화
    pwm = PCA9685()
    # 2. 서보모터 주파수 설정 (일반적으로 50Hz)
    pwm.setPWMFreq(50)
    print("서보모터 회전 시작 (0도 -> 180도)")
    target_channel3 = pca9685.SERVO_MOTOR_PWM3  # 오른쪽 스티어링
    target_channel4 = pca9685.SERVO_MOTOR_PWM4  # 왼쪽 스티어링
    target_channel5 = pca9685.SERVO_MOTOR_PWM5  # 카메라 좌우 스티어링
    target_channel6 = pca9685.SERVO_MOTOR_PWM6  # 카메라 상하 스티어링
    try:
        pwm.setServoPulse(target_channel3, map_angle_to_pulse(90))
        pwm.setServoPulse(target_channel4, map_angle_to_pulse(90))
        pwm.setServoPulse(target_channel5, map_angle_to_pulse(90))
        pwm.setServoPulse(target_channel6, map_angle_to_pulse(90))

        # 전방 스티어링: 오른쪽으로 90도 이동
        for angle in range(90, 181):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel3, pulse_width)
            pwm.setServoPulse(target_channel4, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        time.sleep(1)
        # 전방 스티어링: 오른쪽에서 90도 이동
        for angle in range(180, 91, -1):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel3, pulse_width)
            pwm.setServoPulse(target_channel4, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        time.sleep(1)
        # 전방 스티어링: 왼쪽으로 90도 이동
        for angle in range(90, 1, -1):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel3, pulse_width)
            pwm.setServoPulse(target_channel4, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        time.sleep(1)
        # 전방 스티어링: 왼쪽에서 90도 이동
        for angle in range(1, 91):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel3, pulse_width)
            pwm.setServoPulse(target_channel4, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        print("회전 완료")




        # 카메라 좌우 스티어링: 왼쪽으로 90도 이동
        for angle in range(90, 181):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel5, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        time.sleep(1)
        # 카메라 좌우 스티어링: 왼쪽에서 90도 이동
        for angle in range(180, 91, -1):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel5, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        time.sleep(1)
        # 카메라 좌우 스티어링: 오른쪽으로 90도 이동
        for angle in range(90, 1, -1):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel5, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        time.sleep(1)
        # 카메라 좌우 스티어링: 오른쪽에서 90도 이동
        for angle in range(1, 91):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel5, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)




        # 카메라 상하 스티어링: 위쪽으로 90도 이동
        for angle in range(90, 121):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel6, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        time.sleep(1)
        # 카메라 상하 스티어링: 위쪽에서 90도 이동
        for angle in range(120, 91, -1):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel6, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        time.sleep(1)
        # 카메라 상하 스티어링: 아래쪽으로 90도 이동
        for angle in range(90, 61, -1):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel6, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)
        time.sleep(1)
        # 카메라 상하 스티어링: 아래쪽에서 90도 이동
        for angle in range(60, 91):
            # 각도를 펄스폭(us)으로 변환
            pulse_width = map_angle_to_pulse(angle)
            # 모터 제어
            pwm.setServoPulse(target_channel6, pulse_width)
            # 0.02초 대기 (요청사항)
            time.sleep(0.02)

        print("회전 완료")

        """The following code is applied to
        DC motor control
        """
        # 후방 DC 모터
        pwm.setServoPulse(pca9685.DC_MOTOR_PWM1,15000) # for TB6612 set speed
        # CCW
        pwm.setServoPulse(pca9685.DC_MOTOR_INA1,0) # set INA1 L
        pwm.setServoPulse(pca9685.DC_MOTOR_INA2,19999) # set INA2 H
        print("M1 rotate")
        time.sleep(2)
        # CW
        pwm.setServoPulse(pca9685.DC_MOTOR_INA1,19999) # set INA1 H
        pwm.setServoPulse(pca9685.DC_MOTOR_INA2,0) # set INA2 L
        print("M1 rotate opposite")
        time.sleep(2)
        pwm.setServoPulse(pca9685.DC_MOTOR_PWM1,0) # for TB6612 set speed to 0, stop
        print("M1 stop")
        time.sleep(2)

        # 전방 DC 모터
        pwm.setServoPulse(pca9685.DC_MOTOR_PWM2,15000) # for TB6612 set speed
        # CCW
        pwm.setServoPulse(pca9685.DC_MOTOR_INB1,0) # set INA1 L
        pwm.setServoPulse(pca9685.DC_MOTOR_INB2,19999) # set INA2 H
        print("M2 rotate")
        time.sleep(2)
        # CW
        pwm.setServoPulse(pca9685.DC_MOTOR_INB1,19999) # set INA1 H
        pwm.setServoPulse(pca9685.DC_MOTOR_INB2,0) # set INA2 L
        print("M2 rotate opposite")
        time.sleep(2)
        pwm.setServoPulse(pca9685.DC_MOTOR_PWM2,0) # for TB6612 set speed to 0, stop
        print("M2 stop")
        time.sleep(2)

    except KeyboardInterrupt:
        # Ctrl+C로 중단 시 모터 신호 끄기 (선택사항)
        pwm.setPWM(target_channel3, 0, 0)
        pwm.setPWM(target_channel4, 0, 0)
        pwm.setPWM(target_channel5, 0, 0)
        pwm.setPWM(target_channel6, 0, 0)
        print("\n프로그램 종료")