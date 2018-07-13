##### ShodanAPI
Script que usa a api do shodan para buscar serviços/hosts. 

## Usage:
```
./shodan_api.py <search>
```
 
### Requisitos:
- Módulo shodan
```
pip3 install shodan
```

#### Filters
```
<keyword>:<value>
    city:      find devices in a particular city

    country: find devices in a particular country

    geo: you can pass it coordinates

    hostname: find values that match the hostname

    net: search based on an IP or /x CIDR

    os: search based on operating system

    port: find particular ports that are open

    before/after: find results within a timeframe
```
