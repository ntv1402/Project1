import scrapy


class PopulationSpider(scrapy.Spider):
    name = "population"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
      countries = response.xpath("//td[2]/a")
      populations = response.xpath("//td[3]")
      year_changes = response.xpath("//td[4]")
      net_changes = response.xpath("//td[5]")
      densitys = response.xpath("//td[6]")
      land_areas = response.xpath("//td[7]")
      migrants = response.xpath("//td[8]")
      fert_rates = response.xpath("//td[9]")
      med_ages = response.xpath("//td[10]")
      urban_pops = response.xpath("//td[11]")
      world_shares = response.xpath("//td[12]")

      #for i, country in enumerate(countries):
      #    name = country.xpath(".//text()").get()
      #    population = populations[i].xpath(".//text()").get()
      #    year_change = year_changes[i].xpath(".//text()").get()
      #    net_change = net_changes[i].xpath(".//text()").get()
      #    density = densitys[i].xpath(".//text()").get()
      #    land_area = land_areas[i].xpath(".//text()").get()
      #    migrant = migrants[i].xpath(".//text()").get()
      #    fert_rate = fert_rates[i].xpath(".//text()").get()
      #    med_age = med_ages[i].xpath(".//text()").get()
      #    urban_pop = urban_pops[i].xpath(".//text()").get()
      #    world_share = world_shares[i].xpath(".//text()").get()

      #    yield {
      #        'name': name,
      #        'population': population,
      #        'year_change': year_change,
      #        'net_change': net_change,
      #        'density': density,
      #        'land_area': land_area,
      #        'migrants': migrant,
      #        'fert_rate': fert_rate,
      #        'med_age': med_age,
      #        'urban_pop': urban_pop,
      #        'world_share': world_share,
      #    }
      for i, country in enumerate(countries):
            yield {
            'name': country.xpath(".//text()").get(),
            'population': populations[i].xpath(".//text()").get(),
            'year_change': year_changes[i].xpath(".//text()").get(),
            'net_change': net_changes[i].xpath(".//text()").get(),
            'density': densitys[i].xpath(".//text()").get(),
            'land_area': land_areas[i].xpath(".//text()").get(),
            'migrants': migrants[i].xpath(".//text()").get(),
            'fert_rate': fert_rates[i].xpath(".//text()").get(),
            'med_age': med_ages[i].xpath(".//text()").get(),
            'urban_pop': urban_pops[i].xpath(".//text()").get(),
            'world_share': world_shares[i].xpath(".//text()").get(),
       }
