class Computer {
    constructor(ram, hdd, cpu, type) {
      this.ram = ram;
      this.hdd = hdd;
      this.cpu = cpu;
      this.type = type;
    }
  
    getRam() {
      return this.ram;
    }
  
    getHdd() {
      return this.hdd;
    }
  
    getCpu() {
      return this.cpu;
    }
  
    getType() {
      return this.type;
    }
  
    toString() {
      return `RAM: ${this.ram}GB, HDD: ${this.hdd}GB, CPU: ${this.cpu}GHz, Type: ${this.type}`;
    }
  }
  class PC extends Computer {
    constructor(ram, hdd, cpu) {
      super(ram, hdd, cpu, 'PC');
    }
  }
  
  class Server extends Computer {
    constructor(ram, hdd, cpu) {
      super(ram, hdd, cpu, 'Server');
    }
  }
  class ComputerFactory {
    createComputer(type, ram, hdd, cpu) {
      if (type === 'PC') {
        return new PC(ram, hdd, cpu);
      } else if (type === 'Server') {
        return new Server(ram, hdd, cpu);
      } else {
        throw new Error(`Invalid computer type: ${type}`);
      }
    }
  }
   