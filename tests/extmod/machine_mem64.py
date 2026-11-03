# test machine.mem64

try:
    import machine
    import uctypes

    machine.mem64
except:
    print("SKIP")
    raise SystemExit

import unittest


class Test(unittest.TestCase):
    def test_mem64_print(self):
        self.assertEqual(repr(machine.mem64), "<64-bit memory>")

    def test_operations(self):
        buf = bytearray(16)
        addr = uctypes.addressof(buf)

        machine.mem64[addr] = 0x1122334455667788
        self.assertEqual(machine.mem64[addr], 0x1122334455667788)
        self.assertEqual(buf[:8], b"\x88\x77\x66\x55\x44\x33\x22\x11")

        machine.mem64[addr] = -1
        self.assertEqual(machine.mem64[addr], 0xffffffffffffffff)

    def test_alignment(self):
        buf = bytearray(16)
        addr = uctypes.addressof(buf)

        with self.assertRaises(ValueError):
            machine.mem64[addr + 1]

        with self.assertRaises(ValueError):
            machine.mem64[addr + 1] = 0


if __name__ == "__main__":
    unittest.main()
