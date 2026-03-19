from lerobot.cameras.realsense.camera_realsense import RealSenseCamera
from lerobot.cameras.realsense.configuration_realsense import RealSenseCameraConfig
from lerobot.cameras.configs import ColorMode

# Try using the exact camera name
config = RealSenseCameraConfig(
    serial_number_or_name="Intel RealSense L515",  # ← Exact name from your screenshot
    color_mode=ColorMode.RGB,
    fps=30,
    width=640,
    height=480,
)

print("Creating RealSenseCamera...")
camera = RealSenseCamera(config)

print("Connecting...")
camera.connect()

print("Reading frame...")
frame = camera.read()
print(f"✅ Success! Frame shape: {frame.shape}")

camera.disconnect()