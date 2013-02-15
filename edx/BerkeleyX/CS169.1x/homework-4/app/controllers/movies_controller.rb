class MoviesController < ApplicationController

  def similar
    movie = Movie.find params[:id]
    if movie.director.nil? or movie.director == ''
      flash[:notice] = "'#{movie.title}' has no director info"
      redirect_to movies_path and return
    end
    @movies = Movie.similar_to movie
  end

  def show
    id = params[:id] # retrieve movie ID from URI route
    @movie = Movie.find(id) # look up movie by unique ID
    # will render app/views/movies/show.<extension> by default
  end

  def index
    @all_ratings = Movie.all_ratings
    params[:ratings] = params[:ratings].keys if params[:ratings].is_a?(Hash)
    @ratings = params[:ratings] ? params[:ratings] : (session[:ratings].nil? ? @all_ratings : session[:ratings])
    @order = params[:order] ? params[:order] : (session[:order].nil? ? 'title' : session[:order])
    @movies = Movie.find_all_by_rating @ratings, :order => @order

    if params['ratings'] != @ratings || params[:order] != @order
      flash.keep
      redirect_to :action => 'index', :ratings => @ratings, :order => @order 
    end

    session[:ratings] = @ratings
    session[:order] = @order
  end

  def new
    # default: render 'new' template
  end

  def create
    @movie = Movie.create!(params[:movie])
    flash[:notice] = "#{@movie.title} was successfully created."
    redirect_to movies_path
  end

  def edit
    @movie = Movie.find params[:id]
  end

  def update
    @movie = Movie.find params[:id]
    @movie.update_attributes!(params[:movie])
    flash[:notice] = "#{@movie.title} was successfully updated."
    redirect_to movie_path(@movie)
  end

  def destroy
    @movie = Movie.find(params[:id])
    @movie.destroy
    flash[:notice] = "Movie '#{@movie.title}' deleted."
    redirect_to movies_path
  end

end
