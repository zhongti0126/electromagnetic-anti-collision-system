## 🧩 System Architecture

The system is composed of four main modules:

1. **Distance Sensor Module**  
   Measures the distance between the vehicle and nearby obstacles.

2. **Arduino Control Module**  
   Processes sensor data and determines whether the distance is within the danger range.

3. **Electromagnetic Response Module**  
   Activates the electromagnetic mechanism when a potential collision risk is detected.

4. **Testing & Validation Module**  
   Verifies system stability, response time, and repeated operation reliability.

   ## 🔧 System Flow

```text
[Distance Sensor]
        ↓
[Arduino Controller]
        ↓
[Distance Threshold Judgment]
        ↓
[Electromagnetic Response]
        ↓
[Collision Risk Reduction]

   ## 🌐 API Endpoint

The system provides a simple API to retrieve real-time sensor data

### Endpoint
