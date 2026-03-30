module Jekyll
  class LlmsMarkdownPage < Page
    def initialize(site, base, dir, doc)
      @site = site
      @base = base
      @dir = dir
      @name = "index.html.md"

      self.process(@name)
      self.data = {}
      self.content = render_markdown(doc)
    end

    def render_markdown(doc)
      lines = []
      lines << "# #{doc.data['title']}"
      lines << ""

      if doc.data['date']
        lines << "Date: #{doc.data['date'].strftime('%Y-%m-%d') rescue doc.data['date']}"
      end

      if doc.data['description']
        lines << ""
        lines << "> #{doc.data['description']}"
      end

      if doc.data['cite']
        lines << ""
        lines << "**Citation:** #{doc.data['cite']}"
      end

      if doc.data['team'] && !doc.data['team'].empty?
        team = doc.data['team']
        team_names = team.map do |username|
          member = @site.data['team']&.find { |m| m['username'] == username }
          member ? member['name'] : username
        end
        lines << ""
        lines << "**Authors:** #{team_names.join(', ')}"
      end

      if doc.data['instructors'] && !doc.data['instructors'].empty?
        instructors = doc.data['instructors']
        names = instructors.map do |username|
          member = @site.data['team']&.find { |m| m['username'] == username }
          member ? member['name'] : username
        end
        lines << ""
        lines << "**Instructors:** #{names.join(', ')}"
      end

      if doc.data['code']
        lines << ""
        lines << "**Course code:** #{doc.data['code']}"
      end

      if doc.data['author']
        member = @site.data['team']&.find { |m| m['username'] == doc.data['author'] }
        name = member ? member['name'] : doc.data['author']
        lines << ""
        lines << "**Author:** #{name}"
      end

      if doc.data['tags'] && !doc.data['tags'].empty?
        lines << ""
        lines << "**Tags:** #{doc.data['tags'].join(', ')}"
      end

      if doc.data['links'] && !doc.data['links'].empty?
        lines << ""
        lines << "## Links"
        doc.data['links'].each do |link|
          lines << "- [#{link['text']}](#{link['url']})"
        end
      end

      lines << ""
      lines << doc.content

      if doc.data['statement']
        lines << ""
        lines << "## Data Availability"
        lines << doc.data['statement']
      end

      lines.join("\n")
    end

    def ext
      ".md"
    end

    def output_ext
      ".md"
    end
  end

  class LlmsMarkdownGenerator < Generator
    safe true
    priority :low

    COLLECTIONS = %w[publications courses posts events datasets].freeze

    def generate(site)
      COLLECTIONS.each do |collection_name|
        collection = site.collections[collection_name]
        next unless collection

        collection.docs.each do |doc|
          next unless doc.data['title']

          dir = doc.url.sub(%r{/$}, '')
          page = LlmsMarkdownPage.new(site, site.source, dir, doc)
          site.pages << page
        end
      end
    end
  end
end
