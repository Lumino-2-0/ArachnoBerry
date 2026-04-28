import uasyncio as asyncio
from machine import I2C, Pin
from grove_16_channels_pwm import Grove16PWM

# ================= INIT =================

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=100_000)
pwm = Grove16PWM(i2c)

H_CENTER = 90
V_CENTER = 90

h_angle = H_CENTER
v_angle = V_CENTER


# ================= ASYNC CORE =================

async def _set_leg0(h, v):
    await asyncio.gather(
        pwm.async_servo_angle(0, h, duration_ms=100),
        pwm.async_servo_angle(1, v, duration_ms=100)
    )

async def _set_leg1(h, v):
    await asyncio.gather(
        pwm.async_servo_angle(2, h, duration_ms=100),
        pwm.async_servo_angle(3, v, duration_ms=100)
    )

async def _set_leg2(h, v):
    await asyncio.gather(
        pwm.async_servo_angle(14, h, duration_ms=100),
        pwm.async_servo_angle(15, v, duration_ms=100)
    )

async def _set_leg3(h, v):
    await asyncio.gather(
        pwm.async_servo_angle(12, h, duration_ms=100),
        pwm.async_servo_angle(13, v, duration_ms=100)
    )

async def _set_all_legs(h, v):
    await asyncio.gather(
        _set_leg0(h, v),
        _set_leg1(h, v),
        _set_leg2(h, v),
        _set_leg3(h, v),
    )


# ================= WRAPPERS SYNCHRONES =================

def Servo_test():
    async def _run():
        await _set_all_legs(0, 0)
        await asyncio.sleep(0.5)
        await _set_all_legs(90, 90)
        await asyncio.sleep(0.5)
        await _set_all_legs(180, 180)
        await asyncio.sleep(0.5)

    asyncio.run(_run())


def forward():
    async def _run():
        global h_angle

        await _set_all_legs(h_angle, 60)
        await asyncio.sleep(0.1)

        h_angle = 120
        await _set_all_legs(h_angle, 60)
        await asyncio.sleep(0.1)

        await _set_all_legs(h_angle, 120)
        await asyncio.sleep(0.1)

        h_angle = 60
        await _set_all_legs(h_angle, 120)
        await asyncio.sleep(0.1)

    asyncio.run(_run())


def backward():
    async def _run():
        global h_angle

        await _set_all_legs(h_angle, 60)
        await asyncio.sleep(0.1)

        h_angle = 60
        await _set_all_legs(h_angle, 60)
        await asyncio.sleep(0.1)

        await _set_all_legs(h_angle, 120)
        await asyncio.sleep(0.1)

        h_angle = 120
        await _set_all_legs(h_angle, 120)
        await asyncio.sleep(0.1)

    asyncio.run(_run())


def turn_left():
    async def _run():
        await _set_all_legs(h_angle, 60)
        await asyncio.sleep(0.1)

        await _set_all_legs(60, 60)
        await asyncio.sleep(0.2)

        await _set_all_legs(h_angle, 120)

    asyncio.run(_run())


def turn_right():
    async def _run():
        await _set_all_legs(h_angle, 60)
        await asyncio.sleep(0.1)

        await _set_all_legs(120, 60)
        await asyncio.sleep(0.2)

        await _set_all_legs(h_angle, 120)

    asyncio.run(_run())


def attack():
    async def _run():
        for _ in range(3):
            await _set_all_legs(90, 50)
            await asyncio.sleep(0.15)

            await _set_all_legs(90, 130)
            await asyncio.sleep(0.15)

    asyncio.run(_run())