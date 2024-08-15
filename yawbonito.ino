#include "MPU9250.h"

#define MPU9250_IMU_ADDRESS 0x68

#define MAGNETIC_DECLINATION -2.45 // To be defined by user
#define INTERVAL_MS_PRINT 1000

MPU9250 mpu;

unsigned long lastPrintMillis = 0;


void setup()
{
  Serial.begin(9600);
  Wire.begin();

  Serial.println("Starting...");

  MPU9250Setting setting;

  // Sample rate must be at least 2x DLPF rate
  setting.accel_fs_sel = ACCEL_FS_SEL::A16G;
  setting.gyro_fs_sel = GYRO_FS_SEL::G1000DPS;
  setting.mag_output_bits = MAG_OUTPUT_BITS::M16BITS;
  setting.fifo_sample_rate = FIFO_SAMPLE_RATE::SMPL_250HZ;
  setting.gyro_fchoice = 0x03;
  setting.gyro_dlpf_cfg = GYRO_DLPF_CFG::DLPF_20HZ;
  setting.accel_fchoice = 0x01;
  setting.accel_dlpf_cfg = ACCEL_DLPF_CFG::DLPF_45HZ;

  mpu.setup(MPU9250_IMU_ADDRESS, setting);

  mpu.setMagneticDeclination(MAGNETIC_DECLINATION);
  mpu.selectFilter(QuatFilterSel::MADGWICK);
  mpu.setFilterIterations(20);
 


  Serial.println("Calibration will start in 5sec.");
  Serial.println("Please leave the device still on the flat plane.");
  delay(5000);




  Serial.println("Calibrating...");
  mpu.calibrateAccelGyro();
    
  

  Serial.println("Magnetometer calibration will start in 5sec.");
  Serial.println("Please Wave device in a figure eight until done.");
  delay(5000);

  Serial.println("Calibrating...");
   mpu.calibrateMag();

  Serial.println("Ready!");
  print_calibration();
}

void loop()
{

  unsigned long currentMillis = millis();

  if (mpu.update() && currentMillis - lastPrintMillis > INTERVAL_MS_PRINT) {
   Serial.print("Roll: ");
   Serial.println(mpu.getRoll());
   Serial.print("Yaw: ");
   Serial.println(mpu.getYaw());


    lastPrintMillis = currentMillis;
  }
}




void print_calibration() {
    Serial.println("< calibration parameters >");
    Serial.println("accel bias [mg]: ");
    Serial.print(mpu.getAccBiasX() * 1000.f / (float)MPU9250::CALIB_ACCEL_SENSITIVITY);
    Serial.print(", ");
    Serial.print(mpu.getAccBiasY() * 1000.f / (float)MPU9250::CALIB_ACCEL_SENSITIVITY);
    Serial.print(", ");
    Serial.print(mpu.getAccBiasZ() * 1000.f / (float)MPU9250::CALIB_ACCEL_SENSITIVITY);
    Serial.println();
    Serial.println("gyro bias [deg/s]: ");
    Serial.print(mpu.getGyroBiasX() / (float)MPU9250::CALIB_GYRO_SENSITIVITY);
    Serial.print(", ");
    Serial.print(mpu.getGyroBiasY() / (float)MPU9250::CALIB_GYRO_SENSITIVITY);
    Serial.print(", ");
    Serial.print(mpu.getGyroBiasZ() / (float)MPU9250::CALIB_GYRO_SENSITIVITY);
    Serial.println();
    Serial.println("mag bias [mG]: ");
    Serial.print(mpu.getMagBiasX());
    Serial.print(", ");
    Serial.print(mpu.getMagBiasY());
    Serial.print(", ");
    Serial.print(mpu.getMagBiasZ());
    Serial.println();
    Serial.println("mag scale []: ");
    Serial.print(mpu.getMagScaleX());
    Serial.print(", ");
    Serial.print(mpu.getMagScaleY());
    Serial.print(", ");
    Serial.print(mpu.getMagScaleZ());
    Serial.println();
}